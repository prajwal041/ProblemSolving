from heapq import heappush, heappop, heapify

li = [5,7,9,1,3]

heapify(li)
print("Created heap is = ", end="")
print(li)

heappush(li, 4)
print("Heap after inserting 4 is ", end="")
print(li)

print("Popped smallest element is = ", end="")
print(heappop(li))
