def solution(arr):
    i = 0
    while arr[i] in arr:
        print(arr[i])
        arr[i] = arr[arr[i]+i]
        i = arr[i]
        if arr[i] == i:
            return -1
        # print(i)

def minjumps(arr):
    n = len(arr)
    if n<=1:
        return 0
    if arr[0]==0:
        return -1
    maxreach = arr[0]
    step = arr[0]
    jump = 1
    for i in range(1,n):
        if i==n-1:
            return jump+1
        maxreach = max(maxreach, i+arr[i])
        step-=1
        if step==0:
            jump+=1
            if i>=maxreach:
                return -1
            step=maxreach-i
    return -1


def mysolution(arr):
    i = 0
    jumps = arr[0]
    count = 1
    # print(i, jumps)
    visted = []
    visted.append(i)
    while arr[i] in arr:
        i = arr[jumps]+ arr.index(arr[jumps])
        if i in visted:
            return -1
        visted.append(i)
        jumps= arr[i]
        print(i,jumps)
        if jumps+i >= len(arr):
            return count+2
        count+=1

arr = [2,3,-1,1,3]
# solution(arr)
# print(minjumps(arr))
print(mysolution(arr))