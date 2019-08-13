nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr=list(map(int,input().split()))
f =[]
for _ in range(m):
    a,b,k  = [int(n) for n in input().split()]
    if a == 1:
        arr = arr[b-1:k]+arr[:b-1]+arr[k:]
    elif a == 2:
        arr = arr[:b-1]+arr[k:]+arr[b-1:k]
p=arr[::-1]
print(abs(arr[0]-p[0]))
print(*arr)

'''
Input:
8 4
1 2 3 4 5 6 7 8
1 2 4
2 3 5
1 4 7
2 1 4

Output:
1
2 3 6 5 7 8 4 1
'''


