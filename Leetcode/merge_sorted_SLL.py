# Time T ~ O(n + m)

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def mergeLinkedList(l1, l2):
    l3 = Node(None, None)
    prev = l3

    while l1 is not None and l2 is not None:
        if l1.data < l2.data:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
        prev = prev.next
    if l1 is None: prev.next = l2
    if l2 is None: prev.next = l1

    l3 = l3.next
    while l3 is not None:
        print(f"{l3.data}-->", end="")
        l3 = l3.next

if __name__ == "__main__":
    n3 = Node(10, None)
    n2 = Node(7, n3)
    n1 = Node(1, n2)

    n6 = Node(7, None)
    n5 = Node(5, n6)
    n4 = Node(3, n5)

    mergeLinkedList(n1, n4)