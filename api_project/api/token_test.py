import requests
'''single test to access the api with token authentication'''

headers = {'Authorization': 'Token 441ad133e64f8b2921743236596935f183c740fa'}
response = requests.get('http://127.0.0.1:8000/api/....', headers=headers)
print(response.json())
print(response.status_code)

'''multiple tests to access the api with token authentication'''
TOKEN = '441ad133e64f8b2921743236596935f183c740fa'
headers = {'Authorization': f'Token {TOKEN}'}

endpoints = [
    'http://.../api/endpoint1/',
    'http://.../api/endpoint2/',
    'http://.../api/endpoint3/',
]
for endpoint in endpoints:
    response = requests.get(endpoint, headers=headers)
    print(f'Endpoint: {endpoint}, Status Code: {response.status_code}, Response: {response.json()}')

    try:
        print(response.json())
    except ValueError:
        print(response.text) 
