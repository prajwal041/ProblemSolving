def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(f'Recursion {fib(5)}')

def fibm(n):
    memo = {}
    if n in memo:
        return memo[n]
    if n<2:
        f = 1
    else:
        f = fib(n-1)+fib(n-2)
    memo[n]=f
    return f

print(f'memoization {fibm(5)}')

def bottom(n):
    fib = {}
    for i in range(1,n+1):
        if i<=2:
            f = 1
        else:
            f = fib[i-1]+fib[i-2]
        fib[i] = f
    return fib[n]

print(f'bottom-up {bottom(5)}')