'''
Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA
'''
# def ToString(List):
#     print(''.join(List))
#
# def permute(a,l,r):
#     if l==r:
#         ToString(a)
#     else:
#         for i in range(l,r+1):
#             a[i], a[l] = a[l], a[i]
#             permute(a, l+1, r)
#             a[i], a[l] = a[l], a[i]
#
#
# def solution(nums):
#     for _ in range(nums):
#         s = input()
#         n = len(s)
#         a = list(s)
#         permute(a,0,n-1)
#
#
# n = int(input())
# solution(n)

'''
2nd Approach 

from itertools import permutations
def solution(nums):
    for _ in range(nums):
        s = permutations(input())
        for perm in list(s):
            print(''.join(perm))


n = int(input())
solution(n)
'''

'''
Dynamic Programming approach
'''
def permute(s):
    res = []
    cache = {}
    if len(s)==1:
        res = [s]
        return res
    if s in cache:
        return cache[s]
    else:
        for pos, ch in enumerate(s):
            for perm in permute(s[:pos] + s[pos+1:]):
                res+=[ch+perm]
        cache[s]=res
        return res

def solution(nums):
    for _ in range(nums):
        s = input()
        print(permute(s))


n = int(input())
solution(n)