import requests

parameters = {'car': 2, 'model': 40, 'kim': 30}

response = requests.get('https://httpbin.org/get', params=parameters)

response.raise_for_status()

print(response.text)

