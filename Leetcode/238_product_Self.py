import math
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            left, right = nums[:i], nums[i+1:]

            left_prod, right_prod = math.prod(left), math.prod(right)
            res.append(left_prod*right_prod)
        return res

nums = [1,2,3,4]
s = Solution()
print(s.productExceptSelf(nums))
