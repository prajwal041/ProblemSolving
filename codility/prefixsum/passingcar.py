def solution(a):
    west = 0
    passing = 0
    for i in range(len(a)-1,-1,-1):
        if a[i]==0:
            passing +=west
            if passing >100000000:
                return -1
        else:
            west+=1
    return passing

a = [0,1,0,1,1]
print(solution(a))