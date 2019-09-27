#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    return(len(set(arr).intersection(x+k for x in arr)))

arr = [1,2,3,4]
k=1
print(pairs(k,arr))
