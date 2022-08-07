"""
Question: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
"""

nums = [0,0,1,1,1,2,2,3,3,4]
class Solution:
    def removeDuplicates(self, nums):
        res = []
        for i in nums:
            if i not in res:
                res.append(i)
        nums[:len(res)] = res
        for i in range(len(res), len(nums)):
            nums[i] = '_'
        return len(res), nums


s = Solution()
print(s.removeDuplicates(nums))

