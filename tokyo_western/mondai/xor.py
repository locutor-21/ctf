import sys

lines = open(sys.argv[1]).readlines()
n = len(lines[0])
r="\x00"*n
for line in lines:
	r="".join([chr(ord(line[i])^ord(r[i])) for i in xrange(n-1)])
	print r