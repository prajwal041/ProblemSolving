def solution(s):
    longest = -1
    letters = 0
    digit =0
    other = 0
    for i in s:
        if i.isalpha():
            letters+=1
        elif i.isdigit():
            digit+=1
        elif i ==" ":
            if other==0 and letters%2==0 and digit%2==1:
                if longest < letters+ digit:
                    longest = letters+digit
            digit=letters=other=0
        else:
            other+=1
    return longest

"""
Accurate
"""
def solution1(s):
    return max([len(str) for str in s.split() if len(str) & 1 and str.isalnum() and sum(c.isdigit() for c in str) & 1 ] + [-1])
s="test 5 a0A pass007 ?xy1"
print(solution1(s))


