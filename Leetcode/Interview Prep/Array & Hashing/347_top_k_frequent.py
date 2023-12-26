def topKFrequent(nums, k):
    if len(nums) <= 1:
        return nums
    from collections import Counter
    import heapq

    d = Counter(nums)
    heap = [(val, key) for key, val in d.items()]
    largest = heapq.nlargest(k, heap)
    res = []
    for i in range(k):
        res.append(largest[i][1])
    return res


nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))

'''
Time Complexity: O(K log D + D log D), where D is the count of distinct elements in the array. 

To remove the top of the priority queue O(log d) time is required, so if k elements are removed then O(k log d) time is required, and 
To construct a priority queue with D elements, O(D log D) time is required.
Auxiliary Space: O(D), where D is the count of distinct elements in the array. 
'''