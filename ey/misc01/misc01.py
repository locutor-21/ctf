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

uri = uri_e_host.split()[0][4:]
print "URI=" + uri
#c08a8ea7ba8ea68ebdc08c80818b808a9cc0828e81869f9a838e9d8a82809cc08b8a9c9f8a9d9c80818e8386958a82c1879b8283

host = uri_e_host.split()[2][5:]
print "HOST=" + host
#88899f8d8a85838f958e899ec28e8995898080839bc28f8381c28e9e
