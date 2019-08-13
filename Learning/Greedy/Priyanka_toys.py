n = input()
w = set(map(int, input().split()))

i = 0
while len(w)>0:
    i+=1
    m = min(w)
    w = w.difference(set(range(m, m+5)))
print("Required containers: ",i)

'''
Input:
8
1 2 3 21 7 12 14 21

Output:
4

Time complexicity T ~ O(n)
'''
