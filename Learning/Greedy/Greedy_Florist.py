#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k,li, n):
    if n==k:
        return(sum(li))
    else:
        cost = 0
        li = sorted(li,reverse=True)
        for i in range(n):
            cost+=(i//k+1)*li[i]
        return(cost)

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    li = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, li ,n)
    print(minimumCost)
