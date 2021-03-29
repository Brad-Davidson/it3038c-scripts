import json
import requests

r = requests.get('http://localhost:3000/')
data=r.json()


for widget in data:
    print(f"{widget['name']} is {widget['color']}.")