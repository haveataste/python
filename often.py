import pickle
# 检索所支持的格式
print(pickle.format_version, pickle.compatible_formats)

t = ('this is a string', 42, [1, 2, 3], None)
s = pickle.dumps(t)
p = pickle.loads(s)
print('pickle.dumps(object)', s, 'pickle.loads(pickle_str)', p, sep='\n')

a1 = 'apple'
b1 = {1: 'One', 2: 'Two', 3: 'Three'}
c1 = ['fee', 'fie', 'foe', 'fum']
with open('temp.pkl', 'wb') as f1:
    pickle.dump(a1, f1, True)
    pickle.dump(b1, f1, True)
    pickle.dump(c1, f1, True)
with open('temp.pkl', 'rb') as f2:
    a2 = pickle.load(f2)
    b2 = pickle.load(f2)
    c2 = pickle.load(f2)
print(a2,b2,c2,sep='\n')

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


dir(obj)
help(obj)
callable(obj)
isinstance(obj, typestr)
bin(aint)
oct(aint)
hex(aint)
int(s)
str(aint)
chr(aint)
ord(char)
s.zfill(3)
zip(seq, seq)
enumerate(seq, [start=0])
map(func, seq)
filter(func, seq)
import functools
functools.reduce(func(x,y), seq)
