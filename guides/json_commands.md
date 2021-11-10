# Commands for handling json lines
This is a collection of handy commands for handling large json-line files.

## Splitting a file at a specific point
```
$ head -n 1000 input.json > head.json
$ tail -n +1001 input-json > tail.json
```

## Concatenating a group of files
```
for f in *.json; do (cat "${f}"; echo) >> final.json; done

# This will do the same and will also parse the file so there should not be json errors
cat *.json | jq -c '.' > final.json
```

## Concatenating a few files
```
awk '{print}' a.json b.json > final.json

# This also works but might mess up if there is a newline after the last jsonline
cat a.json <(echo) b.json > final.json
```

## List unique values for key
```
# List all values
cat  a.json |jq -r '.doc_type' > out.json

# Create a unique list of these
cat out.json | sort | uniq -c > final.json
```

## Filtering based on key value
```
# Language confidence above o.5
cat a.json | jq 'select(.lang_fasttext_conf|tonumber >= 0.5)' | jq -s|jq -c .[] > final.json

# Text length longer than 1000 characters
cat a.json | jq 'select(.text|length >= 1000)' | jq -s|jq -c .[] > final.json

# publish year after 1970
cat a.json | jq 'select(.publish_year >= 1970)' | jq -s|jq -c .[] > final.json
```






