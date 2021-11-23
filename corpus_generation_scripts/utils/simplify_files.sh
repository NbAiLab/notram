#!/bin/bash
du -s .
if ! test -d small_files; then
	mkdir small_files

if ! test -f open_books_no.json; then
	awk '{print}' open_books_published_* > open_books_no.json
	mv open_books_published_* small_files/
fi

if ! test -f open_newspapers_no.json; then
	awk '{print}' open_newspapers_published_* > open_newspapers_no.json
	mv open_newspapers_published_* small_files/
fi

if ! test -f open_government_no.json;then
	awk '{print}' open_government_nb.json open_government_nn.json > open_government_no.json
	mv open_government_nb.json small_files/
	mv open_government_nn.json small_files/
fi

if ! test -f open_newspapers_online_no.json;then
	awk '{print}' open_newspapers_online_nb.json open_newspapers_online_nn.json > open_newspapers_online_no.json
	mv open_newspapers_online_nn.json small_files/
	mv open_newspapers_online_nb.json small_files/
fi

if ! test -f open_wikipedia_no.json; then
	awk '{print}' open_wikipedia_nb.json open_wikipedia_nn.json > open_wikipedia_no.json
	mv open_wikipedia_nb.json small_files/
	mv open_wikipedia_nn.json small_files/
fi


if ! test -f restricted_books_no.json; then
        awk '{print}' restricted_books_published_* > restricted_books_no.json
        mv restricted_books_published_* small_files/
fi

if ! test -f restricted_newspapers_no.json; then
        awk '{print}' restricted_newspapers_published_* > restricted_newspapers_no.json
        mv restricted_newspapers_published_* small_files/
fi

if ! test -f external_oscar_no.json;then
        awk '{print}' external_oscar_nb.json external_oscar_nn.json > external_oscar_no.json
        mv external_oscar_nb.json small_files/
        mv external_oscar_nn.json small_files/
fi



du -s .

