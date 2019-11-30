# base case
# self.rear + 1 % self.size == self.front
# 1 2 3 4 5
from collections import deque
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear+1) % self.size == self.front:
            print("Queue is full")
            return
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear+1) % self.size
            self.queue[self.rear] = data

    def deque(self):
        if (self.front == -1):
            print("Queue is empty")
            return
        elif self.front == self.rear:
            val = self.queue[self.front]
            del self.queue[self.front]
            self.front = -1
            self.rear = -1
            return val
        else:
            val = self.queue[self.front]
            del self.queue[self.front]
            self.front = (self.front+1) % self.size
            return val

    def display(self):
        print(self.queue)


if __name__ == "__main__":
    c = CircularQueue(5)
    c.enqueue(1)
    c.enqueue(2)
    c.enqueue(3)
    c.display()
    print(c.deque())
    c.deque()
    c.display()
