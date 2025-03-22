"""
Problem: https://leetcode.com/problems/two-sum/
"""
import time
def calculate_runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Function: {func.__name__} took {run_time} seconds...")
        return result
    return wrapper

@calculate_runtime
def twoSum(nums, target):
    for i, val in enumerate(nums):
        if target - val in nums and nums.index(target - val)!=i:
            return i, nums.index(target - val)

nums = [3,2,4]
target = 6
print(twoSum(nums, target))