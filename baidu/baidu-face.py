import os
from aip import AipFace

os.chdir('D:\\learn\\Python\\baidu\\')

APP_ID = '9762514'
API_KEY = 'BbRDE2RZlikXLpQDqWdBIkxG'
SECRET_KEY = 'mxmOdtAXQ7RR9uV54FQFCsZt7AVa9sTR'
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

options = {
    'max_face_num': 1,
    'face_fields': "age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities",
}

try:
    with open('li.jpg', 'rb') as fp:
        data = fp.read()
    results = aipFace.detect(data, options)
    for key in results:
        print(str(key),'---->',results[key],sep='',end='\n\n')
except IOError as ioerr:
    print('ioerror:',ioerr)


'''
from aip import AipFace

APP_ID = '9762514'
API_KEY = 'BbRDE2RZlikXLpQDqWdBIkxG'
SECRET_KEY = 'mxmOdtAXQ7RR9uV54FQFCsZt7AVa9sTR'
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

options = {
    'max_face_num': 1,
    #'face_fields': "age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities",
    'face_fields': "age,beauty,expression,faceshape,gender,glasses,race,qualities",
}

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

result = aipFace.detect(get_file_content('D:\\learn\\baidu\\li.jpg'), options)
print(result)
'''