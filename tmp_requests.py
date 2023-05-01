import requests


r = requests.get(url='http://127.0.0.1:8000/trades/', params={'limit': 15, 'abc': 100})

a = 0
