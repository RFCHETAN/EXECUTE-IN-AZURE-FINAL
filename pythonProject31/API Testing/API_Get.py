import json

import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

response = requests.get(url)
print(response)
print(response.content)
print(response.headers)

