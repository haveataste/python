import requests
import os
 
sess = requests.session()
url = 'http://asp.cntv.myalicdn.com/asp/hls/2000/0303000a/3/default/b27781706db1474697fcdd0e8153b4ea/2000.m3u8'
s = sess.get(url).content.decode('UTF-8')
fn = [i for i in s.split('\n') if '.ts' in i]
u = 'http://asp.cntv.myalicdn.com/asp/hls/2000/0303000a/3/default/b27781706db1474697fcdd0e8153b4ea/'
ts = [u+i for i in fn]
 
name = '1.ts'
if os.path.exists(name):
    os.remove(name)
fts = open(name, 'ab')
for i in range(len(fn)):
    fts.write(sess.get(ts[i]).content)
    print(fn[i])
fts.close()
os.stat(name)[6]/1024/1024
