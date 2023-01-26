import urllib. request
import os
import random

def url_open(ur1):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36')
    proxies = ['119.6.144.70:81', '111.1.36.9:80', '203.144.144.162:8080']
    proxy = random.choice(proxies) 
    proxy_support = urllib.request.ProxyHandler({'http':proxy})
    opener = urnib.request.build_opener(proxy_support)
    urllib. request. install_opener(opener) 
    response = urllib.request.urlopen(url)
    html = response.read() 
    return html
