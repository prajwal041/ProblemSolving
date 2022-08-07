"""
Problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""
from collections import Counter
def singleNumber(nums):
    for key, val in Counter(nums).items():
        if val == 1:
            return key

def dp(nums):
    return Counter(nums).most_common()[-1][0]

nums = [4,1,2,1,2]
print(singleNumber(nums))
print(dp(nums))
