#!/bin/bash

tshark -r animalcrossing.pcapng -Y "dns && ip.src == 10.1.1.103" | grep quickbrownfoxes | awk "-F " '{print $12}' | awk "-F." '{print $1}' | uniq | base64 -d
