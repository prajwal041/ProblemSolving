def fib(n):
    if n==0 or n==1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    # a,b =0,1
    # for i in range(3, n):
    #     a,b=b,a+b
    #     print(f"b={b}")

n=5
for i in range(n):
    print(fib(i))