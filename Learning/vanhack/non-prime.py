'''
def manipulate_generator(g, n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                # print "Found"
                # g.send(n)
                n = next(g)
                print("no", n)
                # g.send(n)
                # continue
                # yield n
                break
        for i in range(2, n):
            print(f'i={i}')
            if n % i == 0:
                # print(n)
                g.send(n - 1)
                break
    elif n == 1:
        g.send(3)
'''




def manipulate_generator(g, n):
    if n==1:
        g.send(3)
    else:
        if n % 2 == 0:
            n = next(g)
            print("no", n)
            if n % 2 == 0 or n % 3 ==0:
                g.send(n - 1)
            else:
                i = 5
                while (i * i <= n):
                    if (n % i == 0 or n % (i + 2) == 0):
                        g.send(n - 1)
                    i = i + 6
                # for j in range(2, n//2):
                #     print(f'j={j}')
                #
                #     if n % j == 0:
                #         # print(n)
                #         g.send(n - 1)
                #         break








def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1


k = int(input())
g = positive_integers_generator()
for _ in range(k):
    n = next(g)
    print(n)
    manipulate_generator(g, n)