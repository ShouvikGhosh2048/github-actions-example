import os
import requests

with open('page.txt') as f:
    s = f.read()
lines = [line.strip() for line in s.split('\n') if line.strip() != ""]
res = '<ul>'
for line in lines:
    res += '<li>' + line + '</li>'
res += '</ul>'

try:
    response = requests.get('https://cataas.com/cat?json=true').json()
    url = 'https://cataas.com' + response['url']
    res += f'<img src="{url}"/>'
except:
    pass

try:
    os.mkdir('pages')
except:
    pass

with open('pages/index.html', 'w') as f:
    f.write(res)