#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests


url = 'https://ess-kyoo-ell.tjctf.org/'
username = 'username'
password = 'password'



session = requests.Session()
opcoes = session.options(url)
response = session.get(url)

print(opcoes.text)
print("="*30)
print(session.cookies)
print("="*30)
print(response.text)
print("="*30)