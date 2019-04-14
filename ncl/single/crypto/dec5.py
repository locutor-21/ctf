#!/usr/bin/python
import base64

enc = "6fce38f8836e82d446c3af46eb3a945a97bb8088256751e47f73a02943883165"

data = base64.b64decode(enc)

def decode_rc4(key):
	S = range(256)
	j = 0
	out = []

	#KSA Phase
	for i in range(256):
		j = (j + S[i] + ord( key[i % len(key)] )) % 256
		S[i], S[j] = S[j], S[i]

	#PRGA Phase
	i = j = 0
	for char in data:
		i = ( i + 1 ) % 256
	    j = ( j + S[i] ) % 256
	    S[i] , S[j] = S[j] , S[i]
	    out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

	return ''.join(out)

with open("dec5.txt", "r") as dic:
	for key in dic.readlines():
		print "[*] " + decode_rc4(key)
