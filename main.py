import os

with open('page.txt') as f:
    s = f.read()
lines = [line.strip() for line in s.split('\n') if line.strip() != ""]
res = '<ul>'
for line in lines:
    res += '<li>' + line + '</li>'
res += '</ul>'
os.mkdir('pages')
with open('pages/index.html', 'w') as f:
    f.write(res)