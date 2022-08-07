"""
Problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def containsDup(nums):
    checked = set()
    for item in nums:
        if item in checked:
            return True
        else:
            checked.add(item)
    return False

def dp(nums):
    return len(nums) != len(set(nums))

nums = [1,2,3,4]
print(containsDup(nums))