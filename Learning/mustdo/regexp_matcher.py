s = "ab"
p = "."

"""
1. split the patrern w.r.t '*'
2. traverse the pattern front & back of the '*'
    a. do direct match
    b. if we encounter . --> skip that char
    c. if p is "" no comprsion 
"""
flag = 0
for i in range(len(p)):
    if s[i]==p[i]:                      # direct comparision
        pass
    if p[i]=='.':                       # looking for '.' character
        pass
    if p[i]=='*':                       # if we get in '*' in pattern
        m = s.split("*")                # break the pattern into the lists
        b = p[:i]  #[ab]                # before *
        a = p[i+1:]  #[b]               # after *
        x = 0
        for i in range(len(b)):         # loop through after list to the string front side
            if b[i]==s[x]:
                x+=1
                flag =1
            else:
                flag =0
                break
            # print(flag)
            if b[i]=='.':               # looking for '.' character
                x+=1
                flag = 1
        rev = s[::-1]                   # from backward of the string
        y = 0
        for i in range(len(a)):
            if a[i]==rev[y]:
                y+=1
                flag = 1
            else:
                flag = 0
                break
            print(flag)
            if a[i]=='.':               # looking for '.' character
                y+=1
                flag = 1
            if a[i]=='':                # nothing after * so operation required here
                flag=1
                break


if flag ==1:
    print(True)
else:
    print(False)



'''
Input: S-string P-pattern
Output: Boelaen value
constraint: valid pattern, non-empty
edge cases: s ='abab' p='ab*b'

Time T(best) ~ O(n)
     T(avg)  ~ O(n2)
'''