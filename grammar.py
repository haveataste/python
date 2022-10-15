迭代是 python 中访问集合元素的一种非常强大的一种方式。迭代器是一个可以记住遍历位置的对象，因此不会像列表那样一次性全部生成，而是可以等到用的时候才生成，因此节省了大量的内存资源。迭代器对象从集合中的第一个元素开始访问，直到所有的元素被访问完。迭代器有两个方法：iter(iterable)和 next(iterator) 方法。
这么解释可能不太直观，我们以生活的一个小栗子来解释一下，方便大家能够更深刻的理解。比如说我们去超市买水果，而正巧超市的服务人员正在摆放苹果。服务人员告诉我们需要等苹果都摆放完毕我们才可以拿苹果，这样就很耽误我们的时间。(这个场景中，柜台上其实已经有苹果了，只不过销售不让拿罢了。)
然后我们再去卖橘子的柜台，服务人员也在摆放橘子。但是服务人员告诉我们可以不用等他摆放完毕，我们可以直接拿橘子，这样就会很好的节省我们的时间。如果我们拿橘子的速度超过了服务人员摆放的速度 ，我们只需要等待服务人员摆放之后就可以直接拿橘子，大大的提升了我们买橘子的效率。
而迭代器就类似于我们买橘子的场景，我们平时的程序都是一次性写入到内存中。比如我们的列表中存在成百上千的数据，都是一次性写入到内存里的，通过这样让我们来使用。但是迭代器却是按需加载，有一点内容就会放在内容里面，我们就可以立刻使用内存中的数据进行我们的逻辑处理。这样就不要所有的数据都写入到内存中就可以使用，大大的提升了使用效率。
iter(iterable)从可迭代对象中返回一个迭代器,iterable必须是能提供一个迭代器的对象
next(iterator) 从迭代器iterator中获取下一了记录,如果无法获取下一条记录,则触发stoptrerator异常

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
