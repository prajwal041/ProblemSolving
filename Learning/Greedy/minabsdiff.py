def minimumabsdifference(arr):
    arr.sort()
    return(min(abs(arr[i+1]-arr[i]) for i in range(len(arr)-1)))

n = int(input())
arr = list(map(int, input().strip().split()))
result = minimumabsdifference(arr)
print("Minimum :", result)

"""
Input:
10
-59 -36 -13 1 -53 -92 -2 -96 -54 75

Output:
1

T ~ O(n)
S ~ O(1)
"""