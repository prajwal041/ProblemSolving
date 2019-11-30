import gc
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertBefore(self, new):
        new_node = Node(new)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAt(self, prev, new):
        if prev is None:
            print("Prev node is empty")
            return
        new_node = Node(new)
        new_node.next = prev.next
        prev.next = new_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def insertAfter(self, new):
        new_node = Node(new)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next

        last.next = new_node
        new_node.prev = last
        return

    def delete(self, key):
        t = self.head
        if self.head is None or key is None:
            return

        #case 1
        if self.head == key:
            self.head = key.next

        #case 2
        if key.next is not None:
            key.next.prev = key.prev

        #case 3
        if key.prev is not None:
            key.prev.next = key.next

        gc.collect()

    def display(self):
        t = self.head
        while t:
            print(t.data)
            t = t.next

if __name__ == '__main__':
    d = DoublyLinkedList()
    d.insertBefore(1)
    d.insertBefore(2)
    d.insertBefore(3)
    d.insertAt(d.head, 5)
    d.insertAfter(6)
    d.display()
    print("------delete 2------")
    d.delete(d.head.next)
    d.display()

