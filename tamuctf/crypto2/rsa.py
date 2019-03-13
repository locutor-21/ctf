n=2531257
#d=1466291
d=999387
e=43
c="906851 991083 1780304 2380434 438490 356019 921472 822283 817856 556932 2102538 2501908 2211404 991083 1562919 38268"

c = c.split()
for s in c:
	m = (int(s) ** d) % n
	print "m = " + str(m)
	print "m = " + str(m%256)
	print chr(m%256)
	#print unichr(m)
	#m1 = int(m / (256*256))
	#m2 = int((m-256*256*m1) / 256)
	#m3 = int(m - 256*256*m1 - 256*m2)
	#print "m1 = " + str(m1)
	#print "m2 = " + str(m2)
	#print "m3 = " + str(m3)
	#msg = str(chr(m1))+str(chr(m2))+str(chr(m3))
	#print msg

	print "==========="


