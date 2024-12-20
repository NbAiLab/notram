[<img align="right" width="150px" src="../images/nblogo.png">](https://ai.nb.no)
# Frequnetly Used JSON-lines Commands
This is a collection of commands we frequently use for handling large json-line files.

## Splitting a File at a Specific Point
```bash
head -n 1000 input.json > head.json
tail -n +1001 input-json > tail.json
```

## Concatenating a Group of Files
```bash
for f in *.json; do (cat "${f}"; echo) >> final.json; done

# This is slower since it parses the files but will also verify that are no json errors
cat *.json | jq -c '.' > final.json
```

## Concatenating a Few Files
```bash
awk '{print}' a.json b.json > final.json

# This also works if you are sure there is no linebreak at the end of the file
cat a.json <(echo) b.json > final.json
```

## List Unique Values for Key
```bash
# Create a list all doc_type values
cat  a.json |jq -r '.doc_type' > out.json

# Create a unique list of these
cat out.json | sort | uniq -c > final.json
```

## Filtering Based on Key Value
```bash
# Language confidence above o.5
cat a.json | jq 'select(.lang_fasttext_conf|tonumber >= 0.5)' | jq -s|jq -c .[] > final.json

# Text length longer than 1000 characters
cat a.json | jq 'select(.text|length >= 1000)' | jq -s|jq -c .[] > final.json

# publish year after 1970
cat a.json | jq 'select(.publish_year >= 1970)' | jq -s|jq -c .[] > final.json
```


## Remove empty lines from JSON lines file
```bash
# There are several reasons empty lines might occure. This is an easy fix. The fix is done in place.
sed -i '/^$/d' target.json
```




