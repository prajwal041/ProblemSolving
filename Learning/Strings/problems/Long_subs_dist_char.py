def longsub(s):
    d = ""
    f = ""
    for i in range(len(s)):
        if s[i] not in f:
            f+=s[i]
            print(f'f in non-repeat = {f}')
        else:
            if len(d)<len(f):
                d =f
                print(f'd = {d}')
            f =f[f.index(s[i])+1::]+s[i]
            print(f'f in repeat = {f}')
    return max(len(d), len(f))

n = int(input())
for _ in range(n):
    s = input()
    print(longsub(s))