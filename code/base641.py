import base64

s = 'abc*&好'
b64 = base64.b64encode(bytes(s,encoding='utf-8'))
print(s)
print(b64)
deb64 = base64.b64decode(b64)
print(deb64)
print(deb64.decode('unicode_escape'))
