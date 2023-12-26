class Solution:
    def isValid(self, s):
        stack = []
        closeToOpen = { ')': '(', '}': '{', ']': '['}
        for item in s:
            if item in closeToOpen:
                if stack and stack[-1] in closeToOpen[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)
        return True if not stack else False


s = "(]"
sol = Solution()
print(sol.isValid(s))

'''
Time & space : O(n)
'''