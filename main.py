import requests

print('Test!@')

url = 'https://www.google.com'
response = requests.get(url)
print(response.status_code)