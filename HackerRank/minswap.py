#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

def minimumSwaps(q):
    count = 0
    i = 0
    while i<len(q):
        if len(q)==7 and i==6:
            break
        if q[i]==(i+1):
            i+=1
        else:
            q[q[i]-1],q[i]=q[i],q[q[i]-1]
            count+=1
    return(count)

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
    print(res)


