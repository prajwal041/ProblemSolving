def solution(a):
    a.sort()
    return max(a[0]*a[1]*a[-1], a[-1]*a[-2]*a[-3])

a=[-3,1,2,-2,5,6]
print(solution(a))