import threading

def func():
    a.append(2)
    a.append(4)
    a.append(6)
    a.append(8)
    print(a)

a = [1,3,5,7]
timer = threading.Timer(3.0, func)
timer.start()
print(a)