def productarr(arr):
    i,t = 1,1
    n = len(arr)
    prod = [1 for i in range(n)]
    for i in range(n):
        prod[i] = t
        t*=arr[i]
    print(prod)
    t = 1
    for i in range(n-1,-1,-1):
        prod[i]*=t
        t*=arr[i]
        print(t)
    return prod

arr = [1,2,3,4,5]
print(productarr(arr))

"""
T ~ O(n)

"""