import requests
import json

BASE = 'http://127.0.0.1:5000/'

data = [
    {'likes': 10, 'name': 'Tim', 'views': 1000},
    {'likes': 10, 'name': 'How To Become An Api Developer', 'views': 1000},
    {'likes': 10, 'name': 'Tim', 'views': 1000}
]

for i in range(len(data)):

    response = requests.put(BASE + 'video/' + str(i), json=data[i])

    if response.status_code // 100 == 2:
        print(f"Success: {response.status_code} - {response.json()}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

input()

response = requests.patch(BASE + 'video/2', {'views': 99})


if response.status_code // 100 == 2:
    print(f"Success: {response.status_code} - {response.json()}")
else:
    print(f"Error: {response.status_code} - {response.text}")
