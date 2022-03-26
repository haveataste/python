import pickle
print(pickle.format_version, pickle.compatible_formats)     # 检索所支持的格式
t = ('this is a string', 42, [1, 2, 3], None), s = pickle.dumps(t), p = pickle.loads(s)
print('pickle.dumps(object)', s, 'pickle.loads(pickle_str)', p, sep='\n')
a1 = 'apple', b1 = {1: 'One', 2: 'Two', 3: 'Three'}, c1 = ['fee', 'fie', 'foe', 'fum']
with open('temp.pkl', 'wb') as f1:
    pickle.dump(a1, f1, True)
    pickle.dump(b1, f1, True)
    pickle.dump(c1, f1, True)
with open('temp.pkl', 'rb') as f2:
    a2 = pickle.load(f2)
    b2 = pickle.load(f2)
    c2 = pickle.load(f2)
print(a2,b2,c2,sep='\n')

import shutil
'''
shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])
Create an archive file (such as zip or tar) and return its name.
base_name is the name of the file to create, including the path, minus any format-specific extension. format is the archive format: one of “zip” (if the zlib module is available), “tar”, “gztar” (if the zlib module is available), “bztar” (if the bz2 module is available), or “xztar” (if the lzma module is available).
root_dir is a directory that will be the root directory of the archive, all paths in the archive will be relative to it; for example, we typically chdir into root_dir before creating the archive.
base_dir is the directory where we start archiving from; i.e. base_dir will be the common prefix of all files and directories in the archive. base_dir must be given relative to root_dir. See Archiving example with base_dir for how to use base_dir and root_dir together.
root_dir and base_dir both default to the current directory.
'''
shutil.make_archive(tarName, 'tar')

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
re.findall(pattern, string)
re.split(pattern, string[, maxsplit=0, flags=0])
re.sub(pattern, repl, string, count=0, flags=0)

import random
random.random()
random.randint(1,20)
random.uniform(10,20)
random.seed(4)
random.choice([1,2,3,4,5,6])
random.shuffle([1,2,3,4,5,7])
random.sample(range(10),3)

from hashlib import *
import random
s = 'abcd'
hf = random.choice([md5(), sha1(), sha256(), sha512()])
hf.update(bytes(s, encoding='utf-8'))
result = hf.hexdigest().upper()
print(hf, result, len(result), sep='\n')

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

import urllib.request
with urllib.request.urlopen(URL) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    data = f.read()
    print('Data:', data.decode('utf-8'))
d = {
    "content": "中文内容信息",
    "charsetSelect": "utf-8",
    "en": "UrlEncode编码"
}
urllib.parse.urlencode(d) #content=%E4%B8%AD%E6%96%87%E5%86%85%E5%AE%B9%E4%BF%A1%E6%81%AF&charsetSelect=utf-8&en=UrlEncode%E7%BC%96%E7%A0%81
urllib.parse.quote('好好学习')

import requests
url = 'https://api.shodan.io/tools/myip'
r = requests.get(url)
r.url, r.headers, r.cookies, r.status_code, r.encoding, r.text, r.content

import requests
import base64
url = 'http://bunker.wlppr.co/01-hfyeo8.png'
r = requests.get(url).content
e = base64.b64encode(r)
print(len(r), len(e), (len(e)-len(r))/len(r), sep=' ')
base64.b64encode('abc'.encode()).decode('utf-8')
base64.encodebytes(r)

import PIL


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
