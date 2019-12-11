# author:ToddCombs
import requests
import json
import base64

url = 'http://newtest.manager.dapengedu.net/oauth/token'
headers = {'Content-type':'application/json;charset=UTF-8'}
username = 'dapengbeijingservice'
password = 'secretservice'
user_info_str = username + ':' + password
user_info = base64.b64encode(user_info_str.encode())
header_info = {

}
authorization = {}
request_param = {'grant_type':'password','username':'18800000000','password':'123456','scope':'serviceclient'}

r = requests.post(url,data=json.dumps(request_param),headers=headers)
print(r.text)

