import time
from threading import Thread

def m():
    while True:
        print(Thread.name, Thread.ident, 'Yes')
        time.sleep(1)
def f():
    while True:
        print(Thread.name, Thread.ident, 'Noo')
        time.sleep(1)

mt = Thread(target=m, args=())
ft = Thread(target=f, args=())
mt.start()
ft.start()

# CPython is Guido van Rossum’s reference version of the Python computing language. It’s most often called simply “Python”; speakers say “CPython” generally to distinguish it explicitly from other implementations.
# GIL(Global Interpreter Lock)是最流程的 CPython 解释器（平常称为 Python）中的一个技术术语，中文译为全局解释器锁，其本质上类似操作系统的 Mutex。GIL 的功能是：在 CPython 解释器中执行的每一个 Python 线程，都会先锁住自己，以阻止别的线程执行。
# 在 Python 多线程中，变量是共享的，这也是相较多进程的一个优点，线程占用资源要少得多，但也导致多个 CPU 同时操作多个线程时会引起结果无法预测的问题，也就是说 Python 的线程不安全。
# 如何解决线程安全问题？CPython 解释器使用了加锁的方法。每个进程有一把锁，启动线程先加锁，结束线程释放锁。
# 计算密集型，用多进程
# IO密集型，用多线程
