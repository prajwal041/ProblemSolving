import heapq
def solution(A, B, C):
    h = [(-val, s) for val, s in [(A, 'a'), (B, 'b'), (C, 'c')] if val > 0]
    heapq.heapify(h)
    print(h)
    res = []
    while h:
        val, char = heapq.heappop(h)
        if res[-2:] == [char, char]:
            if not h: break
            val2, char2 = heapq.heappop(h)
            res.append(char2)
            if val2 + 1 < 0: heapq.heappush(h, (val2 + 1, char2))
            heapq.heappush(h, (val, char))
        else:
            res.append(char)
            if val + 1 < 0: heapq.heappush(h, (val + 1, char))
    return ''.join(res)

a,b,c = 3,1,1
arr = [1,2,3,4]
print(heapq.heapify(arr))
#print(solution(a,b,c))

