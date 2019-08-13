def solution(x,a):
    passable = [False]*x
    uncovered = x
    for i in range(len(a)):
        if a[i]<=0 or a[i]>x:
            return -1
        if passable[a[i]-1]==False:
            passable[a[i]-1]=True
            uncovered-=1
        if uncovered==0:
            return i
    return -1

a = [1,3,1,4,2,3,5,4]
print(solution(5,a))