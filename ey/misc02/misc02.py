#!/usr/bin/environ python

flag = ""

with open('file.txt', 'r') as f:
	while True:
		line = f.readline()
		if not line:
			break
		for c in line.split():
			c = "0x" + c
			flag += str(chr(int(c, 16)))

print flag

length = len(flag.split())

uri_e_host = flag.split()[length-1].decode('base64')
print uri_e_host


uri = uri_e_host.split()[0][4:]
print "Uri:  " + uri
print len(uri)
host = uri_e_host.split()[2][5:]
print "Host: " + host
print len(host)

