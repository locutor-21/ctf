#!/bin/bash

mariadb -p --binary-as-hex -e "SELECT image FROM images;" boom \
	| tail -n 1 > hex.txt

xxd -r -p hex.txt hi-res-ba0782735805201b04a654215730b793_crop_exact.7z

7z e hi-res-ba0782735805201b04a654215730b793_crop_exact.7z

