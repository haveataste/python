import base64
def picture_to_base64encode(picname):
    with open(picname, 'rb') as fin, open(picname+'.txt', 'w') as fout:
        fout.write(base64.b64encode(fin.read()).decode())

def base64encode_to_picture(filename):
    with open(filename, 'r') as fin, open(filename+'.pic', 'wb') as fout:
        fout.write(base64.b64decode(fin.read()))

if __name__ == '__main__':
    print('picname=', end='');picname=input()
    picture_to_base64encode(picname)

    print('filename=', end='');filename=input()
    base64encode_to_picture(filename)

