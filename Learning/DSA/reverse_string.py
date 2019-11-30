def reverse(s):
    return s[::-1]

def rev(s):
    li = ""
    for i in range(len(s)-1,-1,-1):
        li += s[i]
    return li



s = input()
print(f'{s} reversed = {reverse(s)}')
print(rev(s))