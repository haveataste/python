import requests

data = '''
------WebKitFormBoundaryNXTj3P4yUbNxVtSj
Content-Disposition: form-data; name="url"

http://www.x.com
------WebKitFormBoundaryNXTj3P4yUbNxVtSj
Content-Disposition: form-data; name="seltype"

get
------WebKitFormBoundaryNXTj3P4yUbNxVtSj
Content-Disposition: form-data; name="ck"


------WebKitFormBoundaryNXTj3P4yUbNxVtSj
Content-Disposition: form-data; name="header"

Content-Type:application/x-www-form-urlencoded
------WebKitFormBoundaryNXTj3P4yUbNxVtSj
Content-Disposition: form-data; name="parms"


------WebKitFormBoundaryNXTj3P4yUbNxVtSj
Content-Disposition: form-data; name="proxy"


------WebKitFormBoundaryNXTj3P4yUbNxVtSj
Content-Disposition: form-data; name="code"

utf8
------WebKitFormBoundaryNXTj3P4yUbNxVtSj
Content-Disposition: form-data; name="j"

1
------WebKitFormBoundaryNXTj3P4yUbNxVtSj--
'''
data = {"url":"http://www.x.com",
        "seltype":"get",
        "ck":"",
        "header":"Content-Type:application/x-www-form-urlencoded",
        "parms":"",
        "proxy":"",
        "code":"utf8",
        "j":1,
        }
print(data, type(data))
url = 'http://coolaf.com/tool/ajaxgp'
r = requests.post(url, data=data)
print(r.text)
