from hashlib import *
import random

s = 'abcd'
f = random.choice([md5(), sha1(), sha256(), sha512()])
f.update(bytes(s, encoding='utf-8'))
result = f.hexdigest().upper()
print(f, result, len(result), sep='\n')
