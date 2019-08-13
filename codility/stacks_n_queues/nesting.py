def solution(s):
    if len(s)%2==1: return 0
    matched = {")":"("}
    to_push=["("]
    stack = []
    for i in s:
        if i in to_push:
            stack.append(i)
        else:
            if len(stack)==0:
                return 0
            elif matched[i]!=stack.pop():
                return 0
    if len(stack)==0:
        return 1
    else:
        return 0

s = "(()(())())"
s1 = "(()"
print(solution(s1))