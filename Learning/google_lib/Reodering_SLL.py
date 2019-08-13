# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def __init__(self):
        self.head=None
    def reorderList(self):
        """
        Do not return anything, modify head in-place instead.
        """
        list_len = 0
        cur = self.head

        if (not self.head) or (not self.head.next):
            return

        while cur:
            list_len += 1
            cur = cur.next

        half_len = list_len // 2
        dummy_head1 = ListNode(0)  # start to mid
        dummy_head1.next = self.head
        dummy_head2 = ListNode(0)  # mid to end

        cur = self.head
        half_len -= 1
        while cur and half_len:
            half_len -= 1
            cur = cur.next

        p = cur.next
        cur.next = None
        pre = None
        # reverse the dummy_head2
        while p:
            pre, p.next, p = p, pre, p.next
        dummy_head2.next = pre

        p = dummy_head1.next
        q = dummy_head2.next
        cur = dummy_head1
        while p and q:
            cur.next, p.next, cur, p, q = p, q, q, p.next, q.next

        if p:
            cur.next = p
        head = dummy_head1.next

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        t = self.head
        while t:
            print(t.val)
            t = t.next

l = Solution()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)

print("Before")
l.printList()
l.reorderList()
print("Afer")
l.printList()


# import sys
# import io
# import json
#
# def stringToIntegerList(input):
#     return json.loads(input)
#
#
# def stringToListNode(input):
#     # Generate list from the input
#     numbers = stringToIntegerList(input)
#
#     # Now convert that list into linked list
#     dummyRoot = ListNode(0)
#     ptr = dummyRoot
#     for number in numbers:
#         ptr.next = ListNode(number)
#         ptr = ptr.next
#
#     ptr = dummyRoot.next
#     return ptr
#
#
# def listNodeToString(node):
#     if not node:
#         return "[]"
#
#     result = ""
#     while node:
#         result += str(node.val) + ", "
#         node = node.next
#     return "[" + result[:-2] + "]"
#
#
# def readlines():
#     for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
#         yield line.strip('\n')
#
#
# lines = readlines()
# while True:
#     try:
#         line = next(lines)
#         head = stringToListNode(line)
#
#         ret = Solution().reorderList(head)
#
#         out = listNodeToString(head)
#         if ret is not None:
#             print("Do not return anything, modify head in-place instead.")
#         else:
#             print(out)
#     except StopIteration:
#         break