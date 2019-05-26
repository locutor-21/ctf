#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests


url = 'http://programmable_hyperlinked_pasta.tjctf.org'
username = 'username'
password = 'password'

flag = 'tjctf{l0c4l_f1l3_wh4t?}'

session = requests.Session()
opcoes = session.options(url)
response = session.get(url)

print(opcoes.text)
print("="*30)
print(session.cookies)
print("="*30)
print(response.text)
print("="*30)
