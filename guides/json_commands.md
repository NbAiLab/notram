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


