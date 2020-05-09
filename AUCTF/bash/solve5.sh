#!/bin/bash

sudo -u root /home/level5/portforce.sh &

for i in {1024..65500}
do
	echo "$i / 65500"
	result=$(nc localhost $i 2>/dev/null)
	if [[ "$result" == *"easy"* ]] 
	then
		echo "$result"
	fi
done
