#!/bin/bash

while :
do
	x=$RANDOM
	result=$(echo $x | sudo -u level4 /home/level3/passcodes.sh)
	if [[ "$result" == *"AWESOME"* ]]
	then
		echo "$result"
		exit
	fi
done
