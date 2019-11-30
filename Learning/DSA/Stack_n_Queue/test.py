class Circular:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear+1)% self.size == self.front:
            print("Queue is full")
            return
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear+1)%self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Empty queue")
            return
        elif self.front == self.rear:
            val = self.queue[self.front]
            del self.queue[self.front]
            self.front = self.rear = -1
            return val
        else:
            val = self.queue[self.front]
            del self.queue[self.front]
            self.front = (self.front+1)% self.size
            return val

    def display(self):
        print(self.queue)

if __name__ == "__main__":
    c = Circular(5)
    c.enqueue(1)
    c.enqueue(2)
    c.enqueue(3)
    c.display()
    print(c.dequeue())
    c.dequeue()
    c.display()