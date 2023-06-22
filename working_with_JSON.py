import requests
endpoint = 'https://api.kanye.rest/'

response = requests.get(endpoint)

if response.status_code == 200:
    print(response.json())
else:
    print("Error")







