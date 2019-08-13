#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    seen_dict = {}
    for i in range(len(cost)):
        pcost = cost[i]
        compl = money - pcost
        if compl in seen_dict:
            return(cost.index(compl)+1, i+1)
        else:
            seen_dict[pcost]=compl
    # j = 0
    # seen_dict = {}
    # for i in range(len(cost)):
    #     if(money-cost[i]) in cost:
    #         return (i,j+1)
    #         break
    #     else:
    #         seen_dict[cost[i]]=j
    #         print("seen: ",seen_dict)
    #         print("i ",i)
    #         j+=1

if __name__ == '__main__':
    t = int(input())
    li =[]
    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        li = whatFlavors(cost, money)
    for i in li:
        print(i)