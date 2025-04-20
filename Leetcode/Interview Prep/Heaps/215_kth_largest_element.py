class Solution:
    def findKthLargest(self, nums, k):
        import heapq
        nums = [-n for n in nums]
        heapq.heapify(nums)
        for _ in range(k):
            val = heapq.heappop(nums)
        return val * -1

nums = [3,2,3,1,2,4,5,5,6]
k = 4
s = Solution()
print(s.findKthLargest(nums, k))