import heapq
def findKClosest(arr, k):
    return heapq.nsmallest(k, arr, key=lambda x: abs(x-k))[0]

arr = [100, 200, 300]
print(findKClosest(arr, 100))