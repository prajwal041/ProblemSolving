import heapq

li = [5,7,9,1,3]

heapq.heapify(li)

print(f"Heap created: {list(li)}")

print(f"N Largest: {heapq.nlargest(2, li)}")

heapq.heappop(li)
print(list(li))

def largestHappyString(a, b, c):
    res, maxHeap = "", []
    for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
        if count !=0:
            heapq.heappush(maxHeap, (count, char))
    while maxHeap:
        count, char = heapq.heappop(maxHeap)
        if len(res) > 1 and res[-1] == res[-2] == char:
            if not maxHeap:
                break
            count2, char2 = heapq.heappop(maxHeap)
            res+=char2
            count2+=1
            if count2:
                heapq.heappush(maxHeap, (count2, char2))
        else:
            res+=char
            count+=1
        if count:
            heapq.heappush(maxHeap, (count, char))
    return res


a, b, c = 1,1,7
print(largestHappyString(a,b,c))