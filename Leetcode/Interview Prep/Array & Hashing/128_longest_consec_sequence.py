class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        longest = 0
        for item in nums:
            if (item-1) not in numSet:
                length = 0
                while (item+length) in numSet:
                    length+=1
                longest = max(length, longest)
        return longest


nums = [100,4,200,1,3,2]
s = Solution()
print(s.longestConsecutive(nums))

'''
Time & space: O(n)
'''