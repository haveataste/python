import requests

url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
params = {
    'access_token':'25.f5e510c51e5173224bcf5fb450755aa6.315360000.1831289865.282335-10689949',
    'Content-Type':'application/x-www-form-urlencoded'
    }
print('please input the picture\'s url:');params['url']=input()
d = requests.post(url,params=params).json()
try:
    print('文字行数：',d['words_result_num'])
    for i in d['words_result']:
        print(i['words'])
except:
    print(d)
