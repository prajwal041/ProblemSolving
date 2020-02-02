def findkelement(arr, n):
    leftMax = [None] * n
    leftMax[0] = float('-inf')

    for i in range(1, n):
        leftMax[i] = max(leftMax[i-1], arr[i-1])
    rightMin = float('inf')

    for i in range(n-1, -1, -1):
        if leftMax[i] < arr[i] and rightMin > arr[i]:
            return i
        rightMin = min(rightMin, arr[i])
    return -1

arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
n = len(arr)
print(findkelement(arr,n))