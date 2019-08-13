
# -*- coding: utf-8 -*-
"""def manipulate_generator(g,n):
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                #print "Found"
                #g.send(n)
                #next(g)
                n=next(g)
                #continue
                #yield n
                break
        for i in range(2,n):
            if n%i==0:
                print(n)
                break
    elif n==1:
        g.send(3)"""


def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1


def manipulate_generator(g,n):
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                n = next(g)
                break
            if n%i==0:
                g.send(n-1)
                break

                # break

        # for i in range(2,n):
        #     if n%i==0:
        #         g.send(n-1)
        #         break
    elif n==1:
        g.send(3)

k = int(input("Enter the input number : "))
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    manipulate_generator(g,n)