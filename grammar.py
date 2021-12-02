def bar():
    print('i am bar')
def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper
bar = use_logging(bar)
bar()

# @符号是装饰器的语法糖
@use_logging
def bar():
    print("i am bar")
bar()

>>> def b(a):
...     def c():
...         print('aaa')
...         a()
...     return c
... 
>>> @b
... def a():
...     print('bbb')
... 
>>> a()
aaa
bbb

# 闭包
def f1(x):
    def f2(y):
        return y**x
    return f2
f3 = f1(3)
type(f3)
f3(2) == f1(3)(2)

# Using Functions as Decorators
def entryExit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    return new_f
@entryExit
def func1():
    print("inside func1()")
@entryExit
def func2():
    print("inside func2()")
func1()
print(func1.__name__)
func2()
print(func2.__name__)

# Slightly More Useful
class entryExit(object):
    def __init__(self, f):
        self.f = f
    def __call__(self):
        print("Entering", self.f.__name__)
        self.f()
        print("Exited", self.f.__name__)
@entryExit
def func1():
    print("inside func1()")
@entryExit
def func2():
    print("inside func2()")
func1()
print(type(func1))
func2()
print(type(func2))

l=[1,2,3]
l.append(l)
print(l, len(l), len(l[3]), len(l[3][3][3][3]), sep='\n')

# 有了%matplotlib inline就可以省掉plt.show()了
%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
plt.plot((1,2,3),(4,3,-1))
plt.xlabel(u'x zhou')
plt.ylabel(u'y zhou')
#plt.show() 
