class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Circular:
    def __init__(self):
        self.head = None

    def push(self, new):
        new_node = Node(new)
        t = self.head
        new_node.next = self.head
        if self.head is not None:
            while t.next !=self.head:
                t = t.next
            t.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def ToCircular(self, head):
        start = head
        while head.next is not None:
            head = head.next
        head.next = start
        return start

    def delete(self, key):
        t = self.head
        prev = None
        while t:
            if t.data == key and t == self.head:
                #case 1: head is only element
                if t.next == self.head:
                    t = None
                    self.head = None
                    return
                #case 2: there are elements
                else:
                    #traverse & update head; delete head
                    while t.next!=self.head:
                        t = t.next
                    t.next = self.head.next
                    self.head = self.head.next
                    t = None
                    return
            elif t.data == key:
                prev.next = t.next
                t = None
                return
            else:
                if t.next == self.head:
                    break

            prev = t
            t = t.next

    def count(self):
        t = self.head
        if self.head is None:
            return 0
        count = 0
        while True:
            count+=1
            t = t.next
            if t == self.head:
                break
        return count

    def display(self):
        t = self.head
        if self.head is not None:
            while True:
                print(t.data)
                t = t.next
                if t == self.head:
                    break

if __name__ == "__main__":
    c = Circular()
    c.push(1)
    c.push(2)
    c.push(3)
    c.display()

    print("--------")
    c.delete(2)
    c.display()
    print("---count---")
    print(c.count())



