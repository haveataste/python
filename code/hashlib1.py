import hashlib

s = 'abcd'
h = hashlib.md5()
h = hashlib.sha1()
h.update(bytes(s,encoding='utf-8'))
en = h.hexdigest().upper()
print(en,len(en))