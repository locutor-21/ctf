#!/usr/bin/env python

request = ""

with open("hex.txt", "r") as f:
	while True:
		line = f.readline()
		if not line:
			break
		for c in line.split():
			c = '0x' + c
			request += str(chr(int(c, 16)))

print request
print 20*'-'

request = request.split()
decodeBase64 = request[len(request)-1].decode('base64')

uri = decodeBase64.split()[0][4:]
print len(uri)
print "URI=" + uri
print ""

host = decodeBase64.split()[2][5:]
print len(host)
print "HOST=" + host
print 20*'-'

address = host+uri
print len(address)
print "HOST+URI=" + address
print 20*'-'

n=2
for constant in range(128):
	address_decoded = ""
	for c in [address[i:i+n] for i in range(0, len(address), n)]:
		c = "0x" + c
		res = (int(c,16) - constant) % 128
		address_decoded += str(chr(res))
	print str(constant) + ":"
	print address_decoded
	print ""