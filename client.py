import requests
import json

user_data = ['192.168.0.3', 'windows', 'FW-32']
# user_data = ['192.169.0.3', 'Ianiv']

json_data = json.dumps(user_data)
# client_req_post = requests.post('http://127.0.0.1:8000/api/add_device', data=json_data)
client_req_occ = requests.post('http://127.0.0.1:8000/api/occupy_device', data=json_data)
client_req_rec = requests.get('http://127.0.0.1:8000/api/get_devices')

json_req = json.dumps(client_req_rec.json())
print json_req
