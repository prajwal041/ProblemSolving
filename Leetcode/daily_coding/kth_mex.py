"""
Problem: https://practice.geeksforgeeks.org/contest/job-a-thon-exclusive-hiring-challenge-2-for-amazon-alexa/problems/
Input:
N=1 K=3
arr = {7,5,7,1}
output =3
explanation: values not in arr are: 0,2,3,4,5. out of which 3rd smallest=3

N=1, k=1
arr = {2}
output = 0
"""
def kth_mex(arr, N, k):
    max_item = max(arr)
    not_arr = []
    if len(arr)<=1 and arr[0] == 0:
        return len(arr)
    elif len(arr)<=1:
        return 0
    try:
        for item in range(0,max_item):
            if item not in arr:
                not_arr.append(item)
                if len(not_arr) == k:
                    return not_arr[-1]
        print(not_arr)
        return len(arr)+1
    except:
        return len(arr) +1

arr = [2,23,3,6,23,20,22,23,21,29,14,26,22, 12, 20, 29, 25, 16, 13, 29]
N, K= 20, 19
print(kth_mex(arr, N, K))
