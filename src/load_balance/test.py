import urllib.request
import json      

body = {'ids': [12, 14, 50]}  

myurl = "http://localhost/selectNode"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)

import requests
url = "http://localhost/selectNode"
fin = open('x.txt', 'rb')
files = {'file': fin}
try:
	r = requests.post(url, files=files)
	print (r.text)
finally:
	fin.close()