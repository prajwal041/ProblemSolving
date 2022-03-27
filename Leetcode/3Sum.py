'''
Problem: https://leetcode.com/problems/3sum/
'''

def three_sum(nums):
    if len(nums)<=1:
        return []
    res = []
    nums.sort()
    for i, val in enumerate(nums):
        if i>0 and val == nums[i-1]:
            continue
        l,r = i+1, len(nums)-1
        while l<r:
            threeSum = val + nums[l] + nums[r]
            if threeSum <0:
                l+=1
            elif threeSum >0:
                r-=1
            else:
                res.append([val, nums[l], nums[r]])
                l+=1
                while nums[l] == nums[l-1] and l<r:
                    l+=1
    return res

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
