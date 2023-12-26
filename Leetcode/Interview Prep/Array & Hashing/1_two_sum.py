def twoSum(nums, target):
    i = 0
    while i < len(nums):
        if target-nums[i] in nums and nums.index(target-nums[i])!=i:
            return [i, nums.index(target-nums[i])]

        i+=1

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))
