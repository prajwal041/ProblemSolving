class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def removelist(self, node):
        t = self.head

        if t is not None:
            if t.data == node:
                self.head = t.next
                t = None
                return
        while t is not None:
            if t.data == node:
                break
            prev = t
            t = t.next
        if t == None:
            return
        prev.next = t.next
        t = None

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

l.removelist(2)
l.printList()