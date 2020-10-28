import requests
  
sess = requests.session()
url = "https://douyin.video996.com/parse"
headers = {
    "Host":"douyin.video996.com",
    "Connection":"keep-alive",
    "Content-Length":"207",
    "Pragma":"no-cache",
    "Cache-Control":"no-cache",
    "Accept":"application/json, text/plain, */*",
    "x-appid":"euiFYYbwlv",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Content-Type":"application/json",
    "Origin":"https://douyin.video996.com",
    "Sec-Fetch-Site":"same-origin",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Dest":"empty",
    "Referer":"https://douyin.video996.com/",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cookie":"Hm_lvt_7eb0094a04167581f1abfeea77a8d202=1603892903; Hm_lpvt_7eb0094a04167581f1abfeea77a8d202=1603892903",
}
data = {
    "url":"https://v.douyin.com/JdefVrP/",
    "t":1603895625,
    "n":4293180094,
    "sign":"44c8fc2beff859bddb2c9ff494a4c54ea7378739a1b4054823f3bc260b152ce29e4cfe66af6da0e84aa6c455aecd7f72d76aec0f84623b78e692c77068f66616"
}
res = sess.post(url, headers=headers, data=data)
print(res.text)
