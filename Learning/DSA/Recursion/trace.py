def trace(n):
    if n>0:
        trace(n - 1)
        trace(n - 1)
        print(f"n={n}")



n = 3
trace(n)