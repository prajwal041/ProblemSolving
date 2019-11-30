def fact(n):
    res = 1

    for i in range(2,n+1):
        res = res *i
    return res

def combination(n,r):
    return fact(n)/(fact(r) * fact(n-r))

n,r = 5,3
print(combination(n,r))