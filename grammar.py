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
>>> 
>>> @b
... def a():
...     print('bbb')
... 
>>> a()
aaa
bbb


l=[1,2,3]
l.append(l)
print(l, len(l), len(l[3]), len(l[3][3][3][3]), sep='\n')
