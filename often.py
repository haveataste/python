from numpy import *
zeros((3,4))
ones((2,3,4))
empty((2,3))
random.random((2,3))
arange(1,20,3)
arange(12).reshape(4,3)
arange(24).reshape(2,3,4)

a = arange(1,10).reshape(3,3)
a.sum(), a.min(), a.max(), a.shape, a.size, a.dtype, a.itemsize, a.ndim, a.data
b = ones((3,3))
print(a+b)


import pickle
t = ('this is a string', 42, [1, 2, 3], None)
s = pickle.dumps(t)
po = pickle.loads(s)
print(s,po,sep='\n')


import queue
q = queue.Queue()
for i in range(5):
    q.put(i)
while not q.empty():
    print(q.get())
q = queue.LifoQueue()
for i in range(5):
    q.put(i)
while not q.empty():
    print(q.get())


import sys
sys.version
sys.version_info
sys.path


import sqlite3
conn = sqlite3.connect('name.db')
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
cur.execute('''
''')
cur.executescript('''
''')
cur.fetchone()
conn.commit()
cur.close()
conn.close()


import re
re.compile(r'')
re.search(pattern, string)
re.match(pattern, string).group(2)
re.findall()
re.split(pattern, string[, maxsplit=0, flags=0])
re.sub('', '', s)
re.subs('', '', s)


import random
random.random()
random.randint(1,20)
random.uniform(10,20)
random.seed(4)
random.choice([1,2,3,4,5,6])
random.shuffle([1,2,3,4,5,7])
random.sample(range(10),3)


import time
time.sleep(3)
list(time.localtime())
time.time()


import json
l = json.loads(s)
json.dumps(l)


import string
string.printable
string.punctuation
string.digits
string.ascii_letters
string.capwords('abc def')
string.whitespace
dir(string)


import os
os.name
os.getcwd()
os.listdir()
os.path.abspath('.')
os.path.split(path)
os.path.basename(path)
os.path.dirname(path)
os.path.exists(path)
os.path.getsize(path)
os.path.getmtime(path)
os.path.getatime(path)
os.path.getctime(path)


import PIL


import requests
url = 'https://api.shodan.io/tools/myip'
r = requests.get(url)
r.url, r.headers, r.cookies, r.status_code, r.encoding, r.text, r.content


bin()
oct()
hex()
int()
str()
chr()
ord()
s.zfill(3)

enumerate(sequence, [start=0])
map(func, seq)
filter(func, seq)
import functools
functools.reduce()
