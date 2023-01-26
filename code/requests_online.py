import requests
import re #Regular Expression Module

def baidu():
    res = requests.get("https://www.baidu.com")
    print(type(res),res.status_code,res.encoding,type(res.text),res.cookies,sep='\n')

def qiushibaike():
    #import urllib.request as urllib2
    page = 1
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        print(response)
    except urllib2.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

def poj():
    #http://poj.org/searchuser?key=csuft&field=school&B1=GO
    url = 'http://poj.org/searchuser'
    payload = {'key':'csuft','field':'school','B1':'GO'}
    r = requests.get(url,params=payload,timeout=5).text
    s = r.find('center')-1
    e = r.find('center',s+6)-2
    pattern = re.compile(r'<[^>]+>',re.S)
    r = pattern.sub('',r[s:e])
    print(r)
    try:
        with open('a.txt','w') as data:
            data.write(r.content)
    except IOError as ioerr:
        print(ioerr)

def huoche():
    try:
        r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
        print(r.text)
    except requests.exceptions.SSLError as e:
        print(e)

def hbrk():
    try:
        for i in range(110,151):
            u = 'http://www.hbsoft.net/ws/kaoshi/article.asp?id='+str(i)
            r = requests.get(u)
            s=r.text.find('right')
            if s != -1:
                r.encoding = 'gb2312'
                s=r.text.find('right',s+5)
                e=r.text.find('/table',s)
                g = re.compile(r'<[^>]+>',re.S)
                r = g.sub('',r.text[s:e])
                print(r)
    except:
        print('error')

def dzxm():
    try:
        payload = {
            'dzxm':'%u5218%u76FE',
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400',
            'Cookie':'JSESSIONID=abcx9DgOY24Kkbqb8r_hw'
            }
        r = requests.post('http://222.22.255.106:8089/opac/dzxmjsjg.jsp', data=payload)
        print(r.text)
    except requests.exceptions as e:
        print(e)

def hbrcsc():
    from bs4 import BeautifulSoup
    url = 'http://www.job98.com/templates/_Common/Query/Utils.ashx'
    params = {'tName':'QueryFlow','txtName':'刘盾','txtPerId':'421126199411067218'}
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'}
    r = requests.post(url,params=params,headers=headers).text
    print(r)
    '''
    soup = BeautifulSoup(r,'lxml')
    print(soup.prettify())
    print(soup.get_text())
    '''
    
if __name__ == '__main__':
    hbrcsc()
    print("\nend")
