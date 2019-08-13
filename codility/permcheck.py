def solution(a):
    xor_sum = 0
    for i in range(len(a)):
        xor_sum=xor_sum^a[i]^(i+1)
    if xor_sum!=0:
        return 0
    else:
        return 1

a = [1,2,3,5]
print(solution(a))