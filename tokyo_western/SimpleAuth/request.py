#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
# import re

url = 'http://simpleauth.chal.ctf.westerns.tokyo/'
user = 'admin'
password = 'pass'

session = requests.Session()
opcoes = session.options(url)
response = session.post(url, data={'user': user, 'pass': password})

print(opcoes.text)
print("="*30)
print(response.text)
