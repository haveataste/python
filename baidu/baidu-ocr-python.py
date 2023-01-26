from aip import AipOcr

APP_ID = '10689949'
API_KEY = '0n5Q9qFVP3SxwbS2ihygzy4e'
SECRET_KEY = '2eIgq31blgLj4yRRWcYTELjV8G4Htks9'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}
try:
    with open('mmexport1530493258432.jpg', 'rb') as fp:
        data = fp.read()
    result = aipOcr.basicGeneral(data, options)
    print('文字行数：',result['words_result_num'])
    for i in result['words_result']:
        print(i['words'])
    print(result)
except IOError as ioerr:
    print('ioerror:',ioerr)
except:
    print('other error!')
