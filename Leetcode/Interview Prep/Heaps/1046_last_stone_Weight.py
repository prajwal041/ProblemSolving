class Solution:
    def lastStoneWeight(self, stones):
        import heapq
        if len(stones) == 0:
            return 0
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(x, y)
            diff = abs(x-y)
            heapq.heappush(stones, -diff)
        return abs(stones[0])

stones = [3,7,2] #[2,7,4,1,8,1]
s = Solution()
print(s.lastStoneWeight(stones))
