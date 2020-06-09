import requests
import os
 
sess = requests.session()
url = "https://douyin.video996.com/parse"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
    "Referer": "https://douyin.video996.com/",
}
data = {
    "n": "467497864",
    "sign": "5c3d95d52eab5ffe0f9a2512a79770aec24af7e21667a4b64cc32a90ca72c973e1c4f0f698f236b63825c21e517e82de222f21da310626eff5779e45f0a0315f",
    "t": "1591706008",
    "url": "https://v.douyin.com/JdeFg1s/"
}
res = sess.post(url, headers=headers, data=data)
print(res.text)
