#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import re

username = 'natas20'
password = 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()
response = session.get(url, auth = (username, password))
content = response.text

print(content)
