import sqlite3
conn = sqlite3.connect('name.db')
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
re.search()
re.match()
re.findall()

import random
random.random()
random.randint(1,20)
random.uniform(10,20)
random.seed(4)
random.choice([1,2,3,4,5,6])
random.shuffle([1,2,3,4,5,7])
random.sample([],3)

import time
time.sleep(3)
time.localtime()
time.time()

import json
l = json.loads(s)
json.dumps(l)

import string
string.printable
string.punctuation
string.digits
string.ascii_letters
string.whitespace

import os
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
