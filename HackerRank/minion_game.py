def minion(string):
    n = len(string)
    vowels = "AEIOU"
    k = 0
    s = 0
    for i in range(n):
        if string[i] in vowels:
            k+=n-i
        else:
            s+=n-i
    if s>k:
        print(f'Stuart {s}')
    elif s<k:
        print(f'Kevin {k}')
    else:
        print('Draw')

s = "BANANA"
minion(s)