def mean(a,n):
    return sum(a)/n

from heapq import heapify
def median(a, n):
    heapify(a)
    if n%2!=0:
        return a[int(n/2)]
    return (a[int((n-1)/2)] + a[int((n)/2)])/2.0

def median_array(arr):
    n = len(arr)
    if n%2!=0:
        return arr[int(n/2)]
    return arr[int((n-1)/2)]

arr = [1,2,5]
n = len(arr)
print(mean(arr,n))
print(median(arr,n))
print(f'median of array {arr}= {median_array(arr)}')