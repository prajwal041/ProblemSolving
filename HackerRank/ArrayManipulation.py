#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import accumulate
# # Complete the arrayManipulation function below.          Efficiency  T ~ O(n^2)
# def arrayManipulation(n, queries):
#     li = [0]*(n+1)
#     # for i in queries:
#     #     t = li[i[0]-1:i[1]]
#     #     p = i[0]-1
#     #     while(p< i[1]):
#     #         li[p]+=i[2]
#     #         p+=1
#     return(max(li))
#
#
# if __name__ == '__main__':
#
#     nm = input().split()
#
#     n = int(nm[0])
#
#     m = int(nm[1])
#
#     queries = []
#
#     for _ in range(m):
#         queries.append(list(map(int, input().rstrip().split())))
#
#     result = arrayManipulation(n, queries)
#
#     print(result)

# Efficiency  T ~ O(n)
if __name__ == "__main__":
    n, m = [int(n) for n in input().split()]
    l = [0]*(n+1)
    for _ in range(m):
        a, b, k = [int(n) for n in input().split()]
        l[a-1] += k
        l[b] -= k
    print(l)

    print(max(accumulate(l)))