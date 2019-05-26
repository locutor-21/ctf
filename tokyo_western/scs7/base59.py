from sys import argv

s = argv[1]

r = 1
n = 0

for c in s:
	n += r * ord(c)
	r *= 0x100

st = []

while n > 0:
	st.append(n % 59)
	n /= 59

st.reverse()
print "".join([str(x) for x in st])