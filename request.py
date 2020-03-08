import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'query':'that movie was boring'})

print(r.json())