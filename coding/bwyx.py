import os, requests
from aip import AipOcr
from bs4 import BeautifulSoup as bf

APP_ID = '10689949'
API_KEY = '0n5Q9qFVP3SxwbS2ihygzy4e'
SECRET_KEY = '2eIgq31blgLj4yRRWcYTELjV8G4Htks9'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

for k in range(1,13):
    input()

    picname = str(k)+'.png'
    os.system('adb shell screencap -p /sdcard/b.png')
    os.system('adb pull /sdcard/b.png ./'+picname)
    with open(picname, 'rb') as fp:
        data = fp.read()
    result = aipOcr.basicGeneral(data)

    w = [i['words'] for i in result['words_result']]
    a=b=2
    if w[2].isdigit():
        a=b=3
    for i in range(len(w)):
        if '?' in w[i]:
            b = i
            break
    if a == b:
        s = w[b]
    else:
        s = ''.join(w[a:b+1])
    (x, y, z) = (w[b+1], w[b+2], w[b+3])
    print(s, w[b+1:b+4])
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.5785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}
    r = requests.get('https://www.baidu.com/s?wd='+s[2:]+' '.join(w[b+1:b+4]), headers=headers)
    soup = bf(r.text, 'html.parser')
    f = soup.find(id='content_left').get_text().replace(' ','').replace('\n','')
    e = {}
    e[x] = (f.count(x[:2])+f.count(x[-2:]))*0.5+f.count(x)*0.5
    e[y] = (f.count(y[:2])+f.count(y[-2:]))*0.5+f.count(y)*0.5
    e[z] = (f.count(z[:2])+f.count(z[-2:]))*0.5+f.count(z)*0.5
    t = e[x]+e[y]+e[z]
    (e[x], e[y], e[z]) = (e[x]/t, e[y]/t, e[z]/t)
    e1 = sorted(e,key=lambda x:e[x],reverse=True)
    for i in e1:
        print((' %s   %.2f') % (i, e[i]))
