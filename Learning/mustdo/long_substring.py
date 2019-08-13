s = "malayalam"
l=[]
f=[]
for i in range(len(s)-1):
    l.append(s[i:])
for i in range(len(l)):
    if s[i] in s[i+1:]:
        f.append(s[i])
print(''.join(f))

'''
Longest subset in the string from Leetcode

Input: s = "banana"
Output: "ana"

T ~ O(n)
S ~ O(n)
'''

