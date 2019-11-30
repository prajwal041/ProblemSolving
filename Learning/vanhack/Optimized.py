from heapq import heappush, heappop
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    heap = []
    for i, c in count.items():
        heappush(heap, (-c, i))  #  MaxHeap, push negative value
    
    res = []
    for _ in range(k):
        # print(heappop(heap))
        res.append(heappop(heap)[1])  # Pop the k leaf node
    return res

if __name__ == "__main__":
    arr = [1, 2, 3, 1, 3]
    k = 2
    print(topKFrequent(arr, k))
