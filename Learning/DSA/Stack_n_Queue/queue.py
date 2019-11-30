from collections import deque
queue = deque()
queue.append("A")
queue.append("B")
queue.append("C")
print(queue)
queue.popleft()
print(queue)

# 2nd Approach
from queue import Queue
q = Queue()
q.put("A")
q.put("B")
q.put("C")
print(q)
