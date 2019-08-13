def solution(a):
    lenth = len(a)
    xor_sum= 0
    for i in range(0,lenth):
        xor_sum = xor_sum^a[i]^(i+1)
    return xor_sum^(lenth+1)

a = [2,1,4,5]
print(solution(a))