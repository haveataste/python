from hashlib import *
import random

s = 'abcd'
hf = random.choice([md5(), sha1(), sha256(), sha512()])
hf.update(bytes(s, encoding='utf-8'))
result = hf.hexdigest().upper()
print(hf, result, len(result), sep='\n')
