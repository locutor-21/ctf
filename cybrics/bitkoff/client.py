import requests

url = "http://45.77.201.191/index.php"

name = 'admin'
pswd = 'admin'
data = {"name": name, "password": pswd}

s = requests.Session()
r = s.post(url, data=data)

print (r.text)
s.close()
