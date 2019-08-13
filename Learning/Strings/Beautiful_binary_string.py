s = input()
s = list(s)
count =0
for i in range(len(s)-2):
    if s[i]=='0' and s[i+1]=='1' and s[i+2]=='0':
        count+=1
        s[i+2]='1'
print(count)
print(s)

'''
to avoid pattern '010' in the string
Input:
0100101010

Output:
3

Time T ~ O(n)
Space S ~ O(n)
'''