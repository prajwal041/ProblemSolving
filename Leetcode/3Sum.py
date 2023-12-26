'''
Problem: https://leetcode.com/problems/3sum/
'''
def getUnique(nums):
    result = []
    for item in nums:
        if item not in result:
            result.append(item)
    return result
def three_sum(nums):
    if len(nums)<=1:
        return []
    res = []
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums)):
        j = i + 1
        k = len(sorted_nums) - 1
        while j < k:
            if sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0:
                res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                j += 1
                k -= 1
            elif sorted_nums[i] + sorted_nums[j] + sorted_nums[k] > 0:
                k -= 1
            elif sorted_nums[i] + sorted_nums[j] + sorted_nums[k] < 0:
                j += 1
    return getUnique(res)

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))

'''
Time : O(nlog(n)) 
Space: O(n)
'''