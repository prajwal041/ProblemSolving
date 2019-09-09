import time
from multiprocessing import Process, Lock, Value

def add_500_mp(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value +=5
        lock.release()

def sub_500_mp(total,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value -=5
        lock.release()

if __name__ == '__main__':
    # total = 500
    total = Value('i', 500)
    lock = Lock()
    add_process = Process(target=add_500_mp, args=(total,lock))
    sub_process = Process(target=sub_500_mp, args=(total,lock))

    add_process.start()
    sub_process.start()

    add_process.join()
    sub_process.join()
    print(total.value)