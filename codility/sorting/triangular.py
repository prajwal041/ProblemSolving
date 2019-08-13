def solution(a):
    alen = len(a)
    if alen <3:
        return 0
    a.sort()
    for i in range(alen-2):
        if a[i]+a[i+1]>a[i+2]:
            return 1
    return 0

a = [10,2,5,1,8,20]
print(solution(a))