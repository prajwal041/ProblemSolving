'''
2
geeksforgeeks
geeks for geeks

Output:
geksfor
geks for
'''
def remove_dup(s):
    d = {}
    for i in s:
        if i not in d:
            d[i]=1
    out = ""
    for i in d.keys():
        out+=i
    return out

'''
Solution 2

from collections import OrderedDict
def remove_duplicate(str1):
  return "".join(OrderedDict.fromkeys(str1))
'''

n = int(input())
for _ in range(n):
    s = input()
    print(remove_dup(s))