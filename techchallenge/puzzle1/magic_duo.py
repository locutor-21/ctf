#!/usr/bin/python

number = 0

for i in range(1, 1000):
	for j in range(i, 1000):
		if i <= j:
			product = i*j
			if product < 1000:
				pred = 0
				condition = True
				for c in str(product):
					if pred >= c:
						condition = False
						break
					else: 
						pred = c
				if condition:
					number += 1

print number
