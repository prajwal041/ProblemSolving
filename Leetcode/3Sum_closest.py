"""
Problem: https://leetcode.com/problems/3sum-closest/
"""

def three_sum_closest(arr, target):
    arr.sort()
    curr = arr[0] + arr[1] + arr[len(arr)-1]
    for i, val in enumerate(arr):
        if i> 0 and val == arr[i-1]:
            continue
        l,r = i+1, len(arr)-1
        while l<r:
            tsum = val + arr[l] + arr[r]
            if abs(tsum-target) < abs(curr-target):
                curr =tsum
            if tsum == target:
                return target
            elif tsum < target:
                l+=1
            else:
                r-=1
    return curr

nums = [-1,2,1,-4]
target = 1
print(three_sum_closest(nums, target))