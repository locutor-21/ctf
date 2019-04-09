#!/usr/bin/python

with open("netflow.txt", "r") as file:
	
	ip_add = {}

	records = 0
	s_flags = 0

	for line in file.readlines():
		records += 1
		line = line.split()
		ip_client = line[4].split(":")[0]
		if ip_client not in ip_add:
			ip_add.update({ip_client: 1})
		else:
			ip_add.update({ip_client: ip_add[ip_client]+1})
		flags = line[7]
		if 'S' in flags:
			s_flags += 1
		
	print "Num. of records: " 		+ str(records)
	print "Num. of unique IPs: " 	+ str(len(ip_add))
	print "Num. of s_flags: " 		+ str(s_flags)
	#for (ip, freq) in ip_add.items():
	#	print str(ip) + ":\t" + str(freq)