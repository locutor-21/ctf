
orig = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
inv = ""
for c in orig:
	inv = c+ inv
print inv

enc = "LFIHKRVHRMWRXZGVZURHHSLIGLUDZGVI"
dec = ""
for i in enc:
	dec = dec + inv[orig.find(i)]

print dec