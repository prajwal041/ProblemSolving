"""
Problem: https://leetcode.com/problems/two-sum/
"""

def twoSum(nums, target):
    for i, val in enumerate(nums):
        if target - val in nums and nums.index(target - val)!=i:
            return i, nums.index(target - val)

nums = [3,2,4]
target = 6
print(twoSum(nums, target))