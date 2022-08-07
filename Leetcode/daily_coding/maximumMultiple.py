"""
Problem: https://practice.geeksforgeeks.org/contest/job-a-thon-exclusive-hiring-challenge-2-for-amazon-alexa/problems/#

Input:
N = 4
A = { -12, 17, -13, 17 }
Output:
-204

Input:
N = 2
A = { 2, 6 }
Output:
12
Explanation:
B = {12}
"""

def maxMultiple(arr):
    n = len(arr)
    i = 0
    prod = []
    while i<n:
        item1 = arr[i]
        item2 = arr[i+1]
        prod.append(item1*item2)
        i=i+2
    return max(prod)
arr = [-12, 17, -13, 17]
print(maxMultiple(arr))