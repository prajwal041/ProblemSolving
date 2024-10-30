lst = [100, 150, 200, 250]
k = 225
import heapq

val = heapq.nsmallest(k,lst, key=lambda x: abs(x-k))[0]
print(val)