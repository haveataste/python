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

# GIL 是最流程的 CPython 解释器（平常称为 Python）中的一个技术术语，中文译为全局解释器锁，其本质上类似操作系统的 Mutex。GIL 的功能是：在 CPython 解释器中执行的每一个 Python 线程，都会先锁住自己，以阻止别的线程执行。
# 计算密集型，用多进程
# IO密集型，用多线程
