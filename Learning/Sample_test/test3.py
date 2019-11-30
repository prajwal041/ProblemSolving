from collections import deque
class queue:
    li = []
    def add(self, item, li):
        li.append(item)
        print(f'{item} inserted into the list, list={li}')

    def remove(self, item, li):
        del li
        # print(f'{item} removed from the list, list={li}')
    def display(self):
        print(li)

q = queue()
li = []
q.add(1, li)
q.add(2, li)
q.remove(2,li)
q.display()

