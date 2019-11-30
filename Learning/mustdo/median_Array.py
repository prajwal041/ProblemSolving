def mean(a,n):
    return sum(a)/n

from heapq import heapify
def median(a, n):
    heapify(a)
    if n%2!=0:
        return a[n/2]
    return (a[int((n-1)/2)] + a[int((n)/2)])/2.0

arr = [1,3,2,5]
n = len(arr)
print(mean(arr,n))
print(median(arr,n))