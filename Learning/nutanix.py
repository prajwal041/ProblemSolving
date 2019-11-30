
# k = 2
#

"""
if null return NULL

1. Counter 1: 2, 2: 10, 3: 5
output = [2,3]

"""
from collections import Counter

def k_most(arr, k):
    output = []
    d = dict(Counter(arr))
    arr_val = list(sorted(Counter(arr).values()))
    arr_val = arr_val[::-1]
    if len(arr_val)>k:
        pop_val = len(arr_val) - k
        for i in range(pop_val):
            arr_val.pop()
    for i in arr_val:
        output.append(list(d.keys())[list(d.values()).index(i)])
    return output
    # print(arr_val)

from heapq import heappop, heappush
def topKelement(arr, k):
    heap = []
    for i, c in Counter(arr).items():
        heappush(heap, (-c, i))
    res = []
    for _ in range(k):
        res.append(heappop(heap)[1])
    return res

arr = [1,2,3,1]
k = 2
output = [1,2]
print(topKelement(arr, k))
# d = {'A':1, 'B': 2, 'C': 2}
# print(list(d.keys())[list(d.values()).index(0)])