#Time complexicity ~~ O(n)
def missing(arr,n):
    for i in range(1,n+1):
        if i not in arr:
            print(i)

p = int(input())
for _ in range(p):
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    missing(arr,n)