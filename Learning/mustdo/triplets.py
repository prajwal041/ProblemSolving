import itertools

def triplets(arr):
    for a,b,c in itertools.combinations(arr,3):
        if pow(a,2) + pow(b, 2) == pow(c,2):
            return True
    return False

arr = list(map(int,input().split()))
# arr =[3,4,5]
print(triplets(arr))