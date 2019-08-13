#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apple = []
    count_orange = []
    for i in apples:
        count_apple.append(a+i)
    for i in oranges:
        count_orange.append(b+i)

    list_AO = list(range(s, t+1))
    print(list_AO)
    print(count_apple)
    print(count_orange)
    apple_set = set(count_apple) & set(list_AO)
    orange_set = set(count_orange) & set(list_AO)

    print(len(apple_set))
    print(len(orange_set))

    print(sum([1 for x in apples if(x+a)>=s and (x+a)<=t]))
    print(sum([1 for x in oranges if(x+b)>=s and (x+b)<=t]))

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
