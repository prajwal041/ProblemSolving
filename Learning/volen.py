# import time
# import threading
# def coroutine():
#     for i in range(10000000):
#         print(i)
#
#
# def delayfunc():
#     i = 0
#     while i<(10000000):
#         threading.Timer(i, delayfunc).start()
#         print(f'{i} seconds have passed\n')
#         i+=60
#
# delayfunc()

from multiprocessing import Process
import time

def coroutine():
    for i in range(1,10000000):
        print(i)
        time.sleep(1)

def delayfunc():
    i = 0
    while i < 100000000:
        print(f'{i} seconds have passed\n')
        i+=3
        time.sleep(3)

if __name__ == "__main__":
    p1 = Process(target=delayfunc)
    p1.start()
    p2 = Process(target=coroutine)
    p2.start()



