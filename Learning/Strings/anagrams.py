# a = input()
# b = input()
#
# com = set(a).intersection(b)
# anagram = sum(min(a.count(char),b.count(char)) for char in com)
# print(anagram)
# print(len(a)+len(b)-2*anagram)

'''
Input:
cde
abc

Output:
4

T ~ (n)

'''
from collections import Counter
def anagram(m,n):
    if Counter(m)==Counter(n):
        print("YES")
    else:
        print("NO")

n = int(input())
for _ in range(n):
    m,n = input().split()
    anagram(m,n)