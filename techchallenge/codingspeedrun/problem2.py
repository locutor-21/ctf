#!/usr/bin/python

arr = [-5, -19, 0, -20, -11, 12, 27, -16, -2, -2, 23, 0, -3, 4, 7, -1, -28, 18, 21, 17, -23, 9, 2,-19, 8]

ln = len(arr)
max = 0
#print ln
for i in range(0, 5):
	max += arr[i]

for i in range(ln - 4):
	teste = 0
	print max
	for j in range(0, 5):
		print str(i+j) + ":\t" + str(arr[i+j])
		teste += arr[i+j]
	print '\n'
	if (teste > max):
		max = teste
print max