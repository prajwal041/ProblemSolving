def solution(k,a):
    count = 0
    for i in a:
        if k-i in a:
            print(a.index(i), a.index(k-i))
            count+=1
    return count

def mysolution(k,a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if k-a[i]==a[j]:
                count+=1
    return count

k=6
arr = [1,8,-3,0,1,3,-2,4,5]
print(mysolution(k,arr))
# print(solution(k,arr))