class Solution:
    def dailyTemp(self, temp):
        res = [0] * len(temp)
        stack = []

        for i, t in enumerate(temp):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res

temperatures = [73,74,75,71,69,72,76,73]
s = Solution()
print(s.dailyTemp(temperatures))

'''
Time & Space: O(n)
'''