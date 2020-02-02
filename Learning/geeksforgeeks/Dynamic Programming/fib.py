def fib(n):
    cache = [1] * (n+1)
    for i in range(2, n+1):
        cache[i] = cache[i-1] + cache[i-2]
    print(cache)
    return cache[n-1]

print(fib(5))