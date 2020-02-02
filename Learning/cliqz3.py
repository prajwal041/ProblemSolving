def solution(n):
    a,b = 0,1
    M = 1000000
    for i in range(0, n):
        a,b = b%M,a%M+b % M
    return a%M

def fibmod(n, m):

    def f(n):
        if n == 0:
            return 0, 1
        else:
            a, b = f(n // 2)
            c = a * (2*b - a) % m
            d = (a**2 + b**2) % m

            if n % 2 == 0:
                return c, d
            else:
                return d, (c + d) % m

    return f(n)[0]


n = 3600000
print(fibmod(n,1000000))
print(solution(n))