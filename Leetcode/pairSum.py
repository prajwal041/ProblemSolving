"""
Write a function that returns the indices of an array Arr for
elements that add up to a given number K
For example:
Given an array: [1,1,2,23,4,9,13,6,9] and K = 10, returns [[0,8],[1,5]
"""
def pairSum(arr, k):
    ans = []
    check = []
    for i,val in enumerate(arr):
        if k-val in set(arr) and val not in set(check):
            ans.append([i, arr.index(k-val)])
            check.append(val)
            check.append(k-val)
    return ans

arr = [1,1,2,23,4,9,13,6,9]
k = 10
print(pairSum(arr, k))


