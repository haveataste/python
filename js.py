# pip install PyExecJS

>>> import execjs
>>> execjs.get().name
'Node.js (V8)'
>>> print(execjs.eval("1+2"))
3
>>> func = execjs.compile(
... '''
... function f(m){
...     return m;
... }
... '''
... )
>>> func.call('f', 'hello world!')
'hello world!'


# pip install selenium
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')

# Headless Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式,增加无界面选项
chrome_options.add_argument('--headless')
# 如果不加这个选项，有时定位会出现问题
chrome_options.add_argument('--disable-gpu')
# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get("https://www.taobao.com/")
print(f"browser text = {browser.page_source}")
browser.quit()