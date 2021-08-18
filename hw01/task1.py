import requests
import json

url = 'https://api.github.com/users/tmmix/repos'

resp = requests.get(url)

repos_json = resp.json()
print(repos_json)
names = []
for repo in repos_json:
    names.append({'name': repo['name']})

print(names)
with open('names.json', 'w') as f:
    json.dump(names, f)
