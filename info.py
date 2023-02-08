# Django Rest Framework
# API

import requests
r = requests.request('GET','http://127.0.0.1:8000/api/')

print(r.text)
