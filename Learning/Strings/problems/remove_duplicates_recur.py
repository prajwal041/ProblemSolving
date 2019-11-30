'''
Input:
2
geeksforgeek
acaaabbbacdddd

Output:
gksforgkf
acac
'''
def remove_duplicate(s):
    out = ""
    j = 0
    while j < len(s):
        a = s[j]
        flag = True
        while j < len(s)-1 and s[j+1]==a:
            j+=1
            flag = False
        if flag:
            out+=s[j]
        j+=1
    if out == s:
        return out
    return remove_duplicate(out)

n = int(input())
for _ in range(n):
    s = input()
    print(remove_duplicate(s))