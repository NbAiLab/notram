#!/bin/bash
du -s .

if ! test -f open_books_no.json; then
	awk '{print}' open_books_published_* > open_books_no.json
	rm open_books_published_*
fi

if ! test -f open_newspapers_no.json; then
	awk '{print}' open_newspapers_published_* > open_newspapers_no.json
	rm open_newspapers_published_*
fi

if ! test -f open_government_no.json;then
	awk '{print}' open_government_nb.json open_government_nn.json > open_government_no.json
	rm open_government_nb.json
	rm open_government_nn.json
fi

if ! test -f open_newspapers_online_no.json;then
	awk '{print}' open_newspapers_online_nb.json open_newspapers_online_nn.json > open_newspapers_online_no.json
	rm open_newspapers_online_nn.json
	rm open_newspapers_online_nb.json
fi

if ! test -f open_wikipedia_no.json; then
	awk '{print}' open_wikipedia_nb.json open_wikipedia_nn.json > open_wikipedia_no.json
	rm open_wikipedia_nb.json
	rm open_wikipedia_nn.json
fi

du -s .

