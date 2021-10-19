import json

import requests

file = open('C:\\Users\\Chetan Ramesh\\Desktop\\Post API\\post.json')

url = "https://reqres.in/api/users/2"

response = requests.post(url)
print(response)
