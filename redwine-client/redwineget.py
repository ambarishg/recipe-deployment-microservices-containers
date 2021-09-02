import requests
import json

url = 'http://localhost:5000/hello'
url = 'http://redwineapp.centralindia.azurecontainer.io:5000/hello'
url = 'http://20.193.227.92:5000/hello'

headers = {'content-type': 'application/text', 'Accept-Charset': 'UTF-8'}
r = requests.get(url,  headers=headers)
print(r, r.text)


