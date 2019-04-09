#!/usr/bin/python 

with open("auth.log", "r") as file:

	ip_add = {}
	invalid_user = {}
	valid_user = {}
	total_attempts = 0

	for line in file.readlines():
		line = line.split()[5:]
		phrase = ""
		for word in line:
			phrase = phrase + word + ' '
		phrase = phrase[:-1]
		#print phrase

		#Invalid user short from 133.130.102.142
		if phrase[:13] == "Invalid user ":
			try:
				ip = phrase[13:].split()[2]
				#if ip not in ip_add:
				#	ip_add.update({ip: 1})
				#else:
				#	ip_add.update({ip: ip_add[ip]+1})

				user = phrase[13:].split()[0]
				if user not in invalid_user:
					invalid_user.update({user: 1})
				else:
					invalid_user.update({user: invalid_user[user]+1})

			except:
				#ip = phrase[13:].split()[1]
				#if ip not in ip_add:
				#	ip_add.update({ip: 1})
				#else:
				#	ip_add.update({ip: ip_add[ip]+1})

				if "" not in invalid_user:
					invalid_user.update({"": 1})
				else:
					invalid_user.update({"": invalid_user[""]+1})

		
		#pam_unix(sshd:auth): authentication failure;
		if phrase[:44] == "pam_unix(sshd:auth): authentication failure;":
			total_attempts += 1
			#print phrase[44:]
			try:
				user = phrase.split()[9][5:]
				if user not in valid_user:
					valid_user.update({user: 1})
				else:
					valid_user.update({user: valid_user[user]+1})
			except:
				pass

			rhost = phrase.split()[8][6:]
			if rhost not in ip_add:
				ip_add.update({rhost: 1})
			else: 
				ip_add.update({rhost: ip_add[rhost]+1})

	#How many different IP addresses attempted to gain unauthorized access to the SSH server?
	print "IP addresses: " + str(len(ip_add))
	#How many different usernames were attempted?
	print "TOTAL usernames: " + str(len(valid_user)+len(invalid_user))
	#How many different VALID usernames were attempted?
	print "VALID usernames: " + str(len(valid_user))
	#What IP address made the most number of attempts?
	sorted_ip = sorted(ip_add, key=ip_add.__getitem__, reverse=True)
	print "MOST attempts ip: " + str(sorted_ip[0])
	#What IP address made the 10th most number of attempts? (If there is a tie, enter any one IP)
	print "10th most attempts ip: " + str(sorted_ip[9])
	for i in sorted_ip:
		print i + ":\t" + str(ip_add[i])
	#What was the 5th most attempted username?
	total_users = dict(valid_user.items()+invalid_user.items())
	ordered_total_users = sorted(total_users, key=total_users.__getitem__, reverse=True)
	#for i in ordered_total_users:
	#	print i + ":\t\t" + str(total_users[i])
	print "5th most attempt user: " + str(ordered_total_users[4])
	print "...ou talvez: " + str(sorted(invalid_user, key=invalid_user.__getitem__, reverse=True)[4])
	#for i in total_users:
	#	print i + ":\t\t" + str(total_users[i])
	#What is the total number of failed attempts (ssh attempt failures)?
	print "FAILED attempts: " + str(total_attempts)