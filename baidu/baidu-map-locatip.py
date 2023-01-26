import requests,json

print('please input a ip:');ip = input()
url = 'http://api.map.baidu.com/location/ip'
params = {'ip':ip, 'ak':'2d3KZwtHTfYry0IrQDrl1tGmVIcFChGO', 'coor':'gcj02'}
d = requests.get(url,params=params).json()
s = json.dumps(d, indent=4, sort_keys=True, ensure_ascii=False)
print(s)

#经纬度
lon,lat = d['content']['point']['x'],d['content']['point']['y']
print(lon,lat)
