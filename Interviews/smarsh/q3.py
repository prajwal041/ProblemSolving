def remove_duplicates(llist):
    current1 = llist.head
    while current1:
        data = current1.data
        current2 = current1.next
        while current2:
            if current2.data == data:
                llist.remove(current2)
            current2 = current2.next
        current1 = current1.next