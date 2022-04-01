"""
Problem: https://leetcode.com/problems/4sum/
"""

def four_sum(arr, target):
    arr.sort()
    res = set()
    for i in range(len(arr)-3):
        for j in range(i+1, len(arr)-2):
            a = i
            b = i+1
            l = b+1
            r = len(arr)-1
            while (a<b and l<r and b<l and b<r):
                tsum = arr[a] + arr[b] + arr[l] + arr[r]
                if tsum< target:
                    l+=1
                elif tsum > target:
                    r-=1
                else:
                    res.add((arr[a], arr[b], arr[l], arr[r]))
                    l+=1
                    r-=1
    return res

nums = [1,0,-1,0,-2,2]
target = 0
print(four_sum(nums, target))