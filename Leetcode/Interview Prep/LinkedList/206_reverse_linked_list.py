'''
https://leetcode.com/problems/reverse-linked-list/description/
'''
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseList(self, head):
        prev, cur = None, head
        while cur:
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
        return prev

head = [1,2,3,4,5]
s = Solution()
print(s.reverseList(head))
