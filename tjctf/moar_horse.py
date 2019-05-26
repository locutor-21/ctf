#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests

url = 'https://moar_horse.tjctf.org/legs'

session = requests.Session()
get = session.get(url)

print("="*30)
print("COOKIES")
print(session.cookies)
print("="*30)
print("GET")
print(get.text)
print("="*30)
