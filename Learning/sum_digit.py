def sum_digit(n,k):
    x = n*k%9
    return(x if x else 9)
nk =input().split()
n = int(nk[0])
k = int(nk[1])
result = sum_digit(n,k)
print(result)

'''
Time complexicity T ~ (n)
Input:
148 2

Output:
8
'''