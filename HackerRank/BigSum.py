ar_count = int(input())
ar = list(map(int, input().rstrip().split()))

def Bigsum(ar):
    sum = 0
    for i in ar:
        sum+=i
    return sum

print(Bigsum(ar))