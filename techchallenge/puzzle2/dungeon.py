#!/usr/bin/python

f = open('dungeon.txt', 'r')
flag = ""

for line in f.readlines():
	if (line != "\n"):
		#print line
		cont = 0
		can_escape = 1
		line.split()
		print line
		for c in line:
			#print c
			if (c == '&'):
				cont += 1
			elif (c == '|'):
				cont += -1

			#print cont
			if cont < 0:
				can_escape = 0
		print 10*"="
		print flag
		flag = flag + str(can_escape)

print flag

f.close()