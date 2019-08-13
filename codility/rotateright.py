def solution(a,k):
    i = 0
    while i<k:
        a = a[-1:] + a[:-1]
        i+=1
    return a

a = [3,8,9,7,6]
print(solution(a,3))