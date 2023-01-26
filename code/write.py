import pickle

try:
    with open('b.txt','wb') as data:
        print(dir(__builtins__),file=data)
        data.write(dir(_builtins_))
        pickle.dump(dir(__builtins__),data)
except IOError as err:
    print('File Error:',err)
    
