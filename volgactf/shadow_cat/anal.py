#!/usr/bin/env python
my_dict = {
	'a': 'a',
	'x': 'b',
	'q': 'c',
	'v': 'h',
	'e': 'i',
	'f': 'j',
	'b': 'k',
	's': 'd',
	'g': 'm',
	'c': 'e',
	'w': 'f',
	'l': 'w',
	't': 'o',
	'o': 'x',
	'h': 'p',
	'm': 'q',
	'p': 'y',
	'y': 'r',
	'u': 't',
	'j': 's',
	'i': 'v',
	'k': 'u',
	'z': '_',
	'_': 'z'
}

flag = ''

f = open('encrypted.txt', 'r')

line = f.readline()
for c in line:
	if c in my_dict:
		flag += my_dict[c]
	else:
		flag += c
		print c
	print flag

f.close()