import requests 
from data import data_in

URL = 'http://127.0.0.1:5000/get_data'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL,headers=headers, json=data) 

r.json()
# r.json()

print(data_in)