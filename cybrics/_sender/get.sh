#!/bin/sh

HOST='136.244.67.129 110'
USER='fawkes'
PASSWD='Combin4t1onXXY'
CMD='RETR 1'

(
echo open "$HOST"
sleep 2
echo "USER $USER"
sleep 2
echo "PASS $PASSWD"
sleep 2
echo "$CMD"
sleep 2
echo "QUIT"
) | telnet
