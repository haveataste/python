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
if __name__ == '__main__':
    mt = Thread(target=m, args=())
    ft = Thread(target=f, args=())
    mt.start()
    ft.start()
