from bs4 import BeautifulSoup as bf
import requests
import os

s = requests.get('https://github.com').text
soup = bf(s, 'lxml')
'''
print(soup.prettify())
a = soup.get_text()
for i in a.split('\n'):
    if i != '':
        print(i)
'''
 
if not os.path.exists('img'):
    os.mkdir('img')
for img in soup.find_all('img'):
    url = img.get('src')
    r = requests.get(url)
    name = 'img/'+os.path.basename(url)
    with open(name, 'wb') as pic:
        pic.write(r.content)
        print(name,'download')
