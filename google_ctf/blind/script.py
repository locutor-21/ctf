#!/usr/bin/env python3

import requests

url = 'https://bnv.web.ctfcompetition.com/api/search'

blindvalues = ['10','120','140','1450','150','1240','12450','1250','240','2450','130','1230','1340','13450','1350','12340','123450','12350','2340','23450','1360','12360','24560','13460','134560','13560']

message = "paris"

blindmap = 

for i in range(0, blindvalues.count())

session = requests.Session()
ret = session.post(url, data= {"message":message})
 
print ret.text
