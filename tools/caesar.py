#!/usr/bin/env python

'''
Created by Locutor on April 14th, 2019
'''

import sys
import string

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase

def cipher(enc, key):
	dec = ""
	for c in enc:
		if c in LOWER:
			c = LOWER[(LOWER.find(c) + int(key)) % 26]
			dec += c
		elif c in UPPER:
			c = UPPER[(UPPER.find(c) + int(key)) % 26]
			dec += c
		else:
			dec += c

	print "[+] Key: " + str(key)
	print "[+] Dec: " + dec + '\n'


def main():
	try:
		if sys.argv[1] == '--key' or sys.argv[1] == '-k':
			key = sys.argv[2]
			if not key.isdigit():
				raise ValueError('Key needs to be an integer')
			enc = sys.argv[3]
			cipher(enc, key)
		else:
			enc = sys.argv[1]
			for key in range(1,26):
				cipher(enc, key)
	except ValueError as err:
		print "[-] " + err
		pass
	except:
		print "[-] " + "Something went wrong"
		print "[*] " + "Usage: caesar.py (--key KEY) string"
		pass


if __name__ == '__main__':
	main()
