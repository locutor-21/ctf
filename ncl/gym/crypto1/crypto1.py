#!/usr/bin/python
import binascii

flag = ''
passwd = '01110011 01100101 01100011 01110101 01110010 01100101 01101100 01111001'

for letter in passwd.split():
	flag += binascii.b2a_qp(letter)

print flag
