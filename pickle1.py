import pickle

s = ('this is a string', 42, [1, 2, 3], None)
s1 = pickle.dumps(s)
print('pickle.dumps(object)', s1, sep='\n')  
print('pickle.loads(pickle_str)', pickle.loads(s1), sep='\n')

a1 = 'apple'  
b1 = {1: 'One', 2: 'Two', 3: 'Three'}  
c1 = ['fee', 'fie', 'foe', 'fum']  
with open('temp.pkl', 'wb') as f1:
    pickle.dump(a1, f1, True)  
    pickle.dump(b1, f1, True)  
    pickle.dump(c1, f1, True)  
with open('temp.pkl', 'rb') as f2:
    a2 = pickle.load(f2)  
    b2 = pickle.load(f2)  
    c2 = pickle.load(f2)  
print(a2,b2,c2,sep='\n')

#检索所支持的格式
print(pickle.format_version, pickle.compatible_formats)

l=[1,2,3]
l.append(l)
print(l)
print(len(l), len(l[3]), len(l[3][3][3][3]))
