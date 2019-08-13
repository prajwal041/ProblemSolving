class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pairwiseSwap(self):
        t = self.head
        if t is None:
            return
        while t is not None and t.next is not None:
            t.data, t.next.data = t.next.data, t.data
            t = t.next.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        t = self.head
        while t:
            print(t.data)
            t = t.next


l = LinkedList()
l.push(5)
l.push(4)
l.push(3)
l.push(2)
l.push(1)

print("Before")
l.printList()
l.pairwiseSwap()
print("Afer")
l.printList()