from heapq import heappop, heapify


def KthLargest(arr, k):
    heap = heapify(arr)
    print(heap)
    if len(arr)>=k:
        return heap[k - 1]
    else:
        return -1


m = int(input())
for _ in range(m):
    k, n = map(int, input().split())
    for _ in range(n):
        arr = list(map(int, input().split()))
        heap_arr = []
        for i in arr:
            heap_arr.append(i)
            print(KthLargest(heap_arr, k))

