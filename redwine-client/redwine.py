import requests
import json

# url = 'http://localhost:5000/predict'
# url = 'http://redwineapp.centralindia.azurecontainer.io:5000/predict'
url ='http://13.71.53.118:5000/predict'

data = [7.3,0.65,0,1.2,0.065,15,21,0.9946,3.39,0.47,11]
j_data = json.dumps(data)
print(j_data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)

predictions =  json.loads(r.text)
predictions = predictions["prediction"].replace("[[","")
predictions = predictions.replace("]]","")
print(predictions)

