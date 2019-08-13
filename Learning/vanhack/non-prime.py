'''
Problem: Generating non-prime no
https://www.hackerrank.com/tests/66g0bossg4s/questions/3lpe25ll8jj

Input: 12
Output:
1
4
6
8
9
10
12
14
15
16
18
20

Time T ~ O(n2), where n is the number of input
'''
# prime = [1]
# for num in range(1,100 + 1):
#    # prime numbers are greater than 1
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                prime.append(num)
#                break
#        else:
#            pass
#        if len(prime)==12:
#            break
# for i in range(len(prime)):
#     print(prime[i])



import itertools
def manipulate_generator(g, n):
    # g.send(10)
    # if n> 1:
    #     flag=0
    #     for i in range(2,n):
    #         if n%i ==0:
    #             flag=1
    #             break
    #         else:
    #             flag=0
    #     if flag==0:
    #         g.send(n+1)
    if n==1:
        g.send(n+2)
    # if n==2 or n==3:
    #     g.send(n+1)
        # g.send(n + 1)
    else:
        for i in range(2,n):
            if n%i==0:
                g.send(n+1)
                break



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







