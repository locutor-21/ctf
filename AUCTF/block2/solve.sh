#!/bin/bash

cat co_block.sql \
	| tail -n +30 \
	| awk "-F " '{print $2 ":" $4}' \
	| grep ":1" \
	| awk "-F," '{print "auctf{" $1 "}"}'

