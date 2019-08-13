'''
https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
'''
def maxlen(arr,n):
    hash_map = {}
    length = 0
    curr_sum = 0
    for i in range(n):
        curr_sum+=arr[i]
        if arr[i] == 0 and length == 0:
            length=1
        if curr_sum == 0:
            length=i+1
        if curr_sum in hash_map and length < i - hash_map[curr_sum]:
            length=i-hash_map[curr_sum]
        else:
            hash_map[curr_sum]=i
    return length
n = int(input())
arr = list(map(int, input().split()))
result = maxlen(arr,n)
print("Maximum length with subarray 0 : ", result)
'''
Input:
8
15  -2  2  -8  1  7  10 23

Output:
5

T ~ O(n)
S ~ O(n)
'''