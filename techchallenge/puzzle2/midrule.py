#!/usr/bin/python
import requests
import json

url = "https://techchallenge.withgoogle.com/midrule/" 

visited = []

s = requests.Session()

def explore(dir, path):
	#print "Trying: " + str(dir) + ", " + str(path)
	if path in visited:
		return

	r = s.get(url+path)
	visited.append(path)
	data = json.loads(r.text)

	try:
		print data['TETRAFORCE']
		print data
		print 10*"="
		return
	except:
		pass

	for i in data:
		explore(i, data[i])


def main():
	explore('Initial', 'start')
	s.close()


if __name__ == '__main__':
	main()
