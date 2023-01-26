import requests
import json
import time
from bs4 import BeautifulSoup

def ipcx():
    r = requests.get('http://2017.ip138.com/ic.asp')
    r.encoding = 'GBK'
    r = r.text
    soup = BeautifulSoup(r,'lxml')
    print(soup.center.get_text())

def daili():
    proxies = {"https":"https://61.142.240.132:808"}
    #proxies = {"http":"http://185.193.208.188:8080"}
    r = requests.get('http://2017.ip138.com/ic.asp',proxies=proxies)
    r.encoding = 'GBK'
    r = r.text
    soup = BeautifulSoup(r,'lxml')
    print(soup.center.get_text())

def js():
    url = 'http://lab.crossincode.com/proxy/get/?num=5'
    r = requests.get(url).text
    print(json.loads(r))

if __name__ == '__main__':
    #ipcx()
    #daili()
    js()
