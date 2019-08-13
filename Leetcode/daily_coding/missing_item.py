# [3, 4, -1, 1] should give 2
# [1, 2, 0] should give 3

def missing(arr):
    arr = sorted(arr)
    arr = [abs(a) for a in arr]
    arr = list(set(arr))
    low = arr[0]
    s= arr[0]
    m = max(arr)
    for i in range(low,len(arr)):
        if arr[i]==s:
            pass
        if arr[i]!=s:
            return s+1
        if arr[i]==m:
            return m+1
        s+=1
    return s

arr = [3,4,1,-1]
print(missing(arr))
