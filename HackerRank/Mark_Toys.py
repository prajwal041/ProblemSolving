#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
#Solution 1
def maximumToys(prices, k):
    prices = sorted(prices)
    li = []
    for i in prices:
        if sum(li)<=k:
            li.append(i)
        else:
            break
    return(len(li)-1)

#Solution 2
'''
def maximumToys(prices, k):
    prices = sorted(prices)
    count = 0
    cost = 0
    for i in prices:
        if cost+ i <=k:
            count+=1
            cost+=i
        else:
            break
    return(count)
        
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
Time T ~ O(n)

Input:
7 50
1 12 5 111 200 1000 10

Output:
4

'''