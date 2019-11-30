class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertBefore(self, new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node

    def insertAt(self, prev, new):
        if prev is None:
            print("Previous node is empty")
        new_node = Node(new)
        new_node.next = prev.next
        prev.next = new_node

    def insertAfter(self, new):
        new_node = Node(new)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def deleteNode(self, key):
        prev = None
        # case 1
        t = self.head
        if t is not None:
            if t.data == key:
                self.head = t.next
                t = None
                return

        # case 2
        while t is not None:
            if t.data == key:
                break
            prev = t
            t = t.next

        # case 3
        if t == None:
            return
        prev.next = t.next
        t = None

    def deleteall(self):
        t = self.head
        while t:
            node = t.next
            del t.data
            t = node

    def count(self):
        t = self.head
        count = 0
        while t:
            count+=1
            t = t.next
        return count

    def recursivecount(self, node):
        if node is None:
            return 0
        return 1 + self.recursivecount(node.next)

    def recurse(self):
        return self.recursivecount(self.head)

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def display(self):
        t = self.head
        while t:
            print(t.data)
            t = t.next

if __name__ == "__main__":
    l = Linkedlist()
    l.insertBefore(1)
    l.insertBefore(2)
    l.insertAfter(3)
    l.insertAfter(4)
    l.display()
    print("----insert node 9------")
    l.insertAt(l.head.next, 9)
    l.display()
    print("----delete node 4-------")
    l.deleteNode(4)
    l.display()
    # l.deleteall()
    # print("-----------")
    # l.display()
    print("---count----")
    print(l.count())
    print(l.recurse())
    print("-----reverse Linked List-------")
    l.reverse()
    l.display()
