def solution(h):
    stack = []
    block = 0
    for i in h:
        while len(stack)!=0 and i <stack[-1]:
            stack.pop()
            block+=1
        if len(stack)==0 or i >stack[-1]:
            stack.append(i)
    block+=len(stack)
    return block

h=[8,8,5,7,9,8,7,4,8]
print(solution(h))
