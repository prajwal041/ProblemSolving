# Recursive method T ~ pow(2,n)
def fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# Iterative method T ~ O(n)
def fib(n):
    a,b =0,1
    for i in range(n):
        a,b=b,a+b
    return a

# Bottom up T ~ O(n)
def fib_bottom_up(n):
    if n==1 or n==2:
        return 1
    bottom=[0]*(n+1)
    bottom[1]=1
    bottom[2]=1
    for i in range(3,n+1):
        bottom[i]=bottom[i-1]+bottom[i-2]
    return bottom[n]

print(fibonacci(5))
print(fib(5))
print(fib_bottom_up(5))

