import requests
import json

#墨迹天气-天气信息服务免费版（经纬度）
#实时天气服务：天气状况、温度、湿度、风向、风力等级 预报天气服务：天气状况、温度、风向、风力等级 （未来3天逐日） 实时空气质量指数
url0 = 'http://apifreelat.market.alicloudapi.com/whapi/json/aliweather/briefforecast3days'
#墨迹天气-天气信息服务专业版（经纬度）
#短时预报
url1 = 'http://aliv8.data.moji.com/whapi/json/aliweather/shortforecast'
#天气预报24小时
url2 = 'http://aliv8.data.moji.com/whapi/json/aliweather/forecast24hours'
#AQI预报5天
url3 = 'http://aliv8.data.moji.com/whapi/json/aliweather/aqiforecast5days'
#天气预警
url4 = 'http://aliv8.data.moji.com/whapi/json/aliweather/alert'
#生活指数
url5 = 'http://aliv8.data.moji.com/whapi/json/aliweather/index'
#天气实况
url6 = 'http://aliv8.data.moji.com/whapi/json/aliweather/condition'
#天气预报15天
url7 = 'http://aliv8.data.moji.com/whapi/json/aliweather/forecast15days'
#限行数据
url8 = 'http://aliv8.data.moji.com/whapi/json/aliweather/limit'
#空气质量指数
url9 = 'http://aliv8.data.moji.com/whapi/json/aliweather/aqi'

data = {'lat':'30.5305915755','lon':'114.3168249755'}
appcode = '7cb9365ef1994289a32d6e00bf0c3b8d'
headers = {'Authorization': 'APPCODE '+appcode, 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
r = requests.post(url0, data=data, headers=headers)
d = r.json()
print(type(d))
print(d['data']['forecast'])
s = json.dumps(d, indent=2, sort_keys=True, ensure_ascii=False)
print(s)

