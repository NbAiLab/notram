import os

class Cleaner:
    def __init__(self):
        self.stoplist_dir = os.path.join(os.path.dirname(__file__), 'stoplists')
        self.STOPWORDS_LOW = 0.30
        self.stoplists = self.fetch_stoplists()    

    def fetch_stoplists(self):
        stoplists = set()
        for file in os.listdir(self.stoplist_dir):
            if file.endswith('.txt'):
                with open(os.path.join(self.stoplist_dir, file), 'r') as f:
                    for word in f.readlines():
                        word = word.strip()
                        stoplists.add(word)
        return stoplists

    def get_stopword_density(self, stoplist, text):
        try:
            words = text.lower().strip().split()
            stopword_count = 0
            for word in words:
                if word in stoplist:
                    stopword_count += 1

            word_count = len(words)
            if word_count == 0:
                stopword_density = 0
            else:
                stopword_density = 1.0 * stopword_count / word_count
        except:
            stopword_density = 0

        return stopword_density

    def clean(self, text):
        # loop through stoplists, look for stop word density for each set until threshold is met, otherwise do not classify
        stop_density = self.get_stopword_density(stoplist=self.stoplists, text=text)

        if stop_density >= self.STOPWORDS_LOW:
            return text
        else:
            return None