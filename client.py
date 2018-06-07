import requests
import json

user_data = {'ip' : '192.168.0.3', 'os': 'windows', 'FW': '32', 'user': ''}
# user_data = {'ip' : '192.169.0.3', 'user': 'Ianiv'}

json_data = json.dumps(user_data, encoding="utf-8")
client_req_post = requests.post('http://127.0.0.1:8000/api/add_device', json=json_data)
# client_req_occ = requests.post('http://127.0.0.1:8000/api/occupy_device', json=json_data)
client_req_rec = requests.get('http://127.0.0.1:8000/api/get_devices')

json_req = client_req_rec.json()
print json_req
