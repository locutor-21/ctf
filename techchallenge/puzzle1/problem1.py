string = "SDWP PBZCNAL IJXNLSJI UIF EYKC SQZUQ"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
size = len(alphabet)

for word in string.split():
	for i in range(size):
		new_word = ""
		for c in word:
			new_word = new_word + alphabet[(alphabet.find(c) + i) % size]
		print new_word
	print 10*'='