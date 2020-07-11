import requests
from aip import AipOcr

sess = requests.session()
headers = {"User_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400"}
url_captcha_image = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'#&0.4254218556575875'
response_captcha_image = sess.get(url_captcha_image, headers=headers, verify=False)
response_captcha_image.encoding = 'utf-8'
if response_captcha_image.status_code == 200:
    with open('captcha_image.png', 'wb') as f:
        f.write(response_captcha_image.content)

APP_ID = '10689949'
API_KEY = '0n5Q9qFVP3SxwbS2ihygzy4e'
SECRET_KEY = '2eIgq31blgLj4yRRWcYTELjV8G4Htks9'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
options = {'detect_direction': 'true', 'language_type': 'CHN_ENG',}
try:
    with open('captcha_image.png', 'rb') as fp:
        data = fp.read()
    result = aipOcr.basicGeneral(data, options)
    title = result['words_result'][0]['words']
    de_index = title.index('的')+1
    print(title[de_index:])
except:
    print('error!')

is_position = [int(i) for i in input().split()]
position = ['37,40','107,40','185,40','257,40','37,116','105,116','187,116','255,116']
answer_position = []
for i in is_position:
    answer_position.append(position[i-1])

# ===================================================================================================================
url_captcha_check = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
data_captcha_check = {'answer':','.join(answer_position), 'login_site':'E', 'rand':'sjrand'}
response_captcha_check = sess.post(url_captcha_check, headers=headers, data=data_captcha_check, verify=False)
#验证结果，4:成功  5:验证失败  7:过期  8:验证码校验失败,信息为空
print(response_captcha_check.text, '\n')

# ===================================================================================================================
url_login = 'https://kyfw.12306.cn/passport/web/login'
data_login = {'username':'我的名字你是知道的', 'password':'我的密码当然不能告诉你啦^_^', 'appid':'otn'}
response_login = sess.post(url_login, headers=headers, data=data_login, verify=False)
print(response_login, '\n')

# ===================================================================================================================
url_uamtk = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
data_uamtk = {'appid':'otn'}
response_uamtk = sess.post(url_uamtk, headers=headers, data=data_uamtk, verify=False)
print(response_uamtk.text, '\n')

# ===================================================================================================================
url_uamauthclient = 'https://kyfw.12306.cn/otn/uamauthclient'
data_uamauthclient = {}
data_uamauthclient['tk'] = response_uamtk.json()["newapptk"]
response_uamauthclient = sess.post(url_uamauthclient, headers=headers, data=data_uamauthclient, verify=False)
print(response_uamauthclient.text, '\n')

# ===================================================================================================================
ok_login = 'https://kyfw.12306.cn/otn/index/initMy12306'
response_ok_login = sess.get(ok_login)
s = response_ok_login.text
print(response_ok_login.status_code, s.find('我的名字'), '\n')
