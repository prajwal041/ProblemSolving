from heapq import heappush, heappop

class Priority_Queue:
    def __init__(self):
        self.arr = []

    def insert(self, item):
        return heappush(self.arr, item)

    def delete(self):
        return heappop(self.arr)

    def display(self):
        print(self.arr)

if __name__ == "__main__":
    p = Priority_Queue()
    p.display()
    p.insert(1)
    p.insert(5)
    p.insert(3)
    p.display()
    p.delete()
    p.display()