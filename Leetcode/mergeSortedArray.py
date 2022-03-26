"""
problem: https://leetcode.com/problems/merge-sorted-array/
Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

arr = [1,2,3,1,3]
k=2

from collections import Counter
from heapq import heappush, heappop

def topKelement(arr, k):
    heap = []
    for i, c in Counter(arr).items():
        heappush(heap, (-c, i))

    res = []

    for _ in range(k):
        res.append(heappop(heap)[1])
    return res

print(topKelement(arr, k))
"""

def merge(arr1, m, arr2, n):
    if len(arr1) == 0 and len(arr2) == 0:
        return []
    sort1 = arr1[:m]
    sort2 = arr2[:n]
    return sorted(sort1 + sort2)

"""
solution2 without modifying arr1
"""
def merge_without_arr2(arr1, m, arr2, n):
    arr1[m:]=arr2
    arr1.sort()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(merge(nums1, m, nums2, n))


