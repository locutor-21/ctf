#!/usr/bin/environ python
import requests

ip 		= "http://192.168.10.119"
port	= ":8080"
uri 	= "/login.jsp"

data = {
	'j_username': 'admin',
	'j_password': 'admin',
	'Log In'	: 1
}


s = requests.Session()

r = s.post(ip+port+uri, data=data)
print r.text

s.close()