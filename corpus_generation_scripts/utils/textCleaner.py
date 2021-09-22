import os
import re
import logging
import unicodedata
from html.parser import HTMLParser
import emoji
import unidecode
from spacy.lang.en import English
import ftfy

logger = logging.getLogger(__name__)

# compile regexes
username_regex = re.compile(r'(^|[^@\w])@(\w{1,15})\b')
url_regex = re.compile(r'((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))')
email_regex = re.compile(r'[\w\.-]+@[\w\.-]+')
control_char_regex = re.compile(r'[\r\n\t]+')

# translate table for punctuation
transl_table = dict([(ord(x), ord(y)) for x, y in zip(u"‘’´“”–-",  u"'''\"\"--")])
# HTML parser
html_parser = HTMLParser()


def cleanTextBlock(text, args):
    #If the line is only a \n it is a doc divider. Just return this
    if text == "\n":
        return text

    #Remove any new lines
    text = text.replace("\n","")

    # Check if this is a digibok reference
    if len(text.split()) == 1 and text.startswith("digibok_"):
        if args.digibok == "keep":
            return text
        if args.digibok == "remove":
            return ""

    if args.standardize:
        text = standardize_text(text)
    if args.replace_usernames:
        text = replace_usernames(text, filler=args.username_filler)
    if args.replace_urls:
        text = replace_urls(text, args.url_filler)
    if args.replace_email:
        text = replace_email(text, args.email_filler)
    if args.asciify_emojis:
        text = asciify_emojis(text)
    if args.standardize_punctuation:
        text = standardize_punctuation(text)
    if args.do_lower_case:
        text = text.lower()
    if args.fix_unicode:
        text = ftfy.fix_text(text)
    if args.replace_multiple_usernames:
        text = replace_multi_occurrences(text, args.username_filler)
    if args.replace_multiple_urls:
        text = replace_multi_occurrences(text, args.url_filler)
    if args.remove_unicode_symbols:
        text = remove_unicode_symbols(text)
    if args.remove_accented_characters:
        text = remove_accented_characters(text)
    if count_alphawords(text) < args.min_alphawords:
        text = ""
    return text


def cleanTextBlock_notram(text, username_filler="@user",url_filler="http://domain.com", email_filler="anonymous@domain.com",
        digibok="keep", minimum_alphawords=2, replace_usernames=False, replace_urls=False, fix_unicode=True, asciify_emoji=True,
        replace_multiple_usernames = False, standardize=True, replace_multiple_urls=False,remove_unicode_symbols=True, remove_accented_characters=False, 
        standardize_punctation=True, do_lower_case=False):
    
    """
    Default settings used in the nortram-modell. Can be called both for creating datasets and for interference
    Input should be a single paragraph with text. Any newlines are stripped.
    Passing an object similar to the one created by ArgParse 
    """

    class ArgsClass:
        pass

    args = ArgsClass()
    args.username_filler = username_filler # Username filler (ignored when replace_username option is False)
    args.url_filler = url_filler # URL filler (ignored when replace_urls option is False)
    args.email_filler = email_filler # Email filler (ignored when replace_email option is False)
    args.digibok = digibok # Handling of digibok_ids. "keep", "remove" or "auto". Last option relies on other settings in script
    args.minimum_words = minimum_words # The minimum number of words in the block to keep it
    args.minimum_alpha = minimum_alpha # The minimum number of alphanum characters in the block to keep it. Removes OCR errors from cover pages.
    args.replace_usernames = replace_usernames # Replace usernames with filler. Mainly for tweets
    args.replace_urls = replace_urls # Replace URLs with filler
    args.replace_email = replace_email # Replace emails with filler
    args.fix_unicode = fix_unicode # Use ftfy to fix and standardise unicode. Converts it all to valid utf-8
    args.asciify_emojis = asciify_emojis # Asciifyi emojis. On by default but mainly useful for social media
    args.replace_multiple_usernames = replace_multiple_usernames #Replace "@user @user" with "2 <username_filler>. Mainly for use on tweets
    args.standardize = standardize # Replace "Standardize text. Remove all control characters.
    args.replace_multiple_urls = replace_multiple_urls # Replace "@user @user" with "2 <username_filler>. Mainly for use on tweets"
    args.remove_unicode_symbols = remove_unicode_symbols # After preprocessing remove characters which belong to unicode category "So"
    args.remove_accented_characters = remove_accented_characters #Remove accents/asciify everything. Not recommended since it interferes with ÅåäÄöÄäÄ
    args.standardize_punctuation = standardize_punctation # Standardize (asciifyi) special punctuation
    args.do_lower_case = do_lower_case #Convert text to lower case

    cleaned = cleanTextBlock(text, args)
    return cleaned


def remove_accented_characters(text):
    text = unidecode.unidecode(text)
    return text

def remove_unicode_symbols(text):
    text = ''.join(ch for ch in text if unicodedata.category(ch)[0] != 'So')
    return text

def replace_multi_occurrences(text, filler):
    """Replaces multiple occurrences of filler with n filler"""
    # only run if we have multiple occurrences of filler
    if text.count(filler) <= 1:
        return text
    # pad fillers with whitespace
    text = text.replace(f'{filler}', f' {filler} ')
    # remove introduced duplicate whitespaces
    text = ' '.join(text.split())
    # find indices of occurrences
    indices = []
    for m in re.finditer(r'{}'.format(filler), text):
        index = m.start()
        indices.append(index)
    # collect merge list
    merge_list = []
    for i, index in enumerate(indices):
        if i > 0 and index - old_index == len(filler) + 1:
            # found two consecutive fillers
            if len(merge_list) > 0 and merge_list[-1][1] == old_index:
                # extend previous item
                merge_list[-1][1] = index
                merge_list[-1][2] += 1
            else:
                # create new item
                merge_list.append([old_index, index, 2])
        old_index = index
    # merge occurrences
    if len(merge_list) > 0:
        new_text = ''
        pos = 0
        for (start, end, count) in merge_list:
            new_text += text[pos:start]
            new_text += f'{count} {filler}'
            pos = end + len(filler)
        new_text += text[pos:]
        text = new_text
    return text

def asciify_emojis(text):
    """
    Converts emojis into text aliases. E.g. 👍 becomes :thumbs_up:
    For a full list of text aliases see: https://www.webfx.com/tools/emoji-cheat-sheet/
    """
    text = emoji.demojize(text)
    return text

def standardize_text(text):
    """
    1) Escape HTML
    2) Replaces some non-standard punctuation with standard versions. 
    3) Replace \r, \n and \t with white spaces
    4) Removes all other control characters and the NULL byte
    5) Removes duplicate white spaces
    """
    # escape HTML symbols
    text = html_parser.unescape(text)
    # standardize punctuation
    text = text.translate(transl_table)
    text = text.replace('…', '...')
    # replace \t, \n and \r characters by a whitespace
    text = re.sub(control_char_regex, ' ', text)
    # remove all remaining control characters
    text = ''.join(ch for ch in text if unicodedata.category(ch)[0] != 'C')
    # replace multiple spaces with single space
    text = ' '.join(text.split())
    return text.strip()

def standardize_punctuation(text):
    return ''.join([unidecode.unidecode(t) if unicodedata.category(t)[0] == 'P' else t for t in text])

def replace_usernames(text, filler='user'):
    # @<user> is a marker used internally. use filler instead
    text = text.replace('@<user>', f'{filler}')
    # replace other user handles by filler
    text = re.sub(username_regex, filler, text)
    # add spaces between, and remove double spaces again
    text = text.replace(filler, f' {filler} ')
    text = ' '.join(text.split())
    return text

def replace_urls(text, filler='url'):
    # <url> is a marker used internally. use filler instead
    text = text.replace('<url>', filler)
    # replace other urls by filler
    text = re.sub(url_regex, filler, text)
    # add spaces between, and remove double spaces again
    text = text.replace(filler, f' {filler} ')
    text = ' '.join(text.split())
    return text

def replace_email(text, filler='email'):
    text = re.sub(email_regex, filler, text)
    # add spaces between, and remove double spaces again
    text = text.replace(filler, f' {filler} ')
    text = ' '.join(text.split())
    return text

def count_alphawords(text):
    #Counts the number of pure alphawords (at least two characters long) in a text string
    #Adds spaces before some characters, if not . and , would lead to non-alpha words
    pat = re.compile(r"([.,;()!:/])")
    text = pat.sub(" \\1 ", text)
    num = sum((w.isalpha() and len(w) >= 2) for w in text.split())
    return num

def count_words(text):
    return len(text.split())

