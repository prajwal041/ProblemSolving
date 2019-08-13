def solution(a):
    head = a[0]
    tail = sum(a[1:])
    min_diff = abs(head-tail)
    for i in range(1, len(a)):
        head+=a[i]
        tail-=a[i]
        if abs(head-tail)<min_diff:
            min_diff=abs(head-tail)
    return min_diff

a = [3,1,2,4,3]
print(solution(a))