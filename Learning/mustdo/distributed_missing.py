def missing(a):
    from heapq import heapify
    miss = [x for x in range(min(a), max(a)) if x not in a]
    if len(miss)==0:
        return a[-1]+1
    heapify(miss)
    return miss[0]

arr = [0, 1, 5, 4, 7, 9]
print(missing(arr))