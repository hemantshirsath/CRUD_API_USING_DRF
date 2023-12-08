import requests
import json


data={
    'id':1,
    'name':"Sonu Shimpi",
    'roll':101,
    'city':"Jadgaon"
}
json_data=json.dumps(data)
response=requests.put('http://127.0.0.1:8000/viewstu/',data=json_data)
data=response.json()
print(data)