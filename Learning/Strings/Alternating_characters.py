s='AAAAA'
count = 0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1

print(count)

'''
Input:
AAAAA

Output:
4

Time T ~ O(n)
Space S ~ O(n)
'''