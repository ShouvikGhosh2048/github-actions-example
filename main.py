with open('page.txt') as f:
    s = f.read()
lines = [line.strip() for line in s.split('\n') if line.strip() != ""]
res = '<ul>'
for line in lines:
    res += '<li>' + line + '</li>'
res += '</ul>'
with open('page.html', 'w') as f:
    f.write(res)