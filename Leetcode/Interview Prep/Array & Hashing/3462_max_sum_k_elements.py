"""
https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/
"""
from typing import List
class Solutions:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int):
        arr = []
        total = 0
        for i in range(len(grid)):
            s = sorted(grid[i], reverse=True)
            arr.extend(s[:limits[i]])
            print(arr, limits[i])
        arr.sort()
        for i in range(k):
            total+=arr.pop()
        return total

grid = [[5,3,7],[8,2,6]]
limits = [2,2]
k = 3
s = Solutions()
print(s.maxSum(grid, limits, k))