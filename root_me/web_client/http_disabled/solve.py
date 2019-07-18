#!/usr/bin python

import requests

addr = 'http://challenge01.root-me.org'
path = '/web-client/ch25'

url = addr + path 
s = requests.Session()
r = s.post(url, data = {"auth-login": "admin"})
print(r.text)

s.close()
