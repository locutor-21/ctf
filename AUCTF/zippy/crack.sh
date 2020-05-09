#!/bin/bash

hashes=$(echo $1 | awk "-F." '{print $1 ".hashes"}')
zip2john $1 > $hashes
john --wordlist=/usr/share/wordlists/rockyou.txt $hashes
password=$(john --show $hashes | head -n 1 | cut -d ":" -f 2)
echo $password
unzip -P $password $1

