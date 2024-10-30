'''
Largest contigeous subarray: https://leetcode.com/problems/maximum-subarray/
Kadane's Algorithm
'''
def max_Array(arr):
    fmax = tmax= start = end = s = 0
    n = len(arr)
    for i in range(len(arr)):
        tmax +=arr[i]
        if tmax < 0:
            tmax = 0
            s = i+1
        if fmax < tmax:
            fmax = tmax
            start = s
            end = i
    if fmax == 0:
        if n == 1:
            return arr[0]
        if arr[0] <= 0:
            return fmax or max(arr)
        return -1
    return fmax or max(arr)
num = [-1,-2]
print(max_Array(num))

'''
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''