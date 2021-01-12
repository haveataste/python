import pickle

# 检索所支持的格式
print(pickle.format_version, pickle.compatible_formats)

t = ('this is a string', 42, [1, 2, 3], None)
s = pickle.dumps(t)
p = pickle.loads(s)
print('pickle.dumps(object)', s, 'pickle.loads(pickle_str)', p, sep='\n')

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
