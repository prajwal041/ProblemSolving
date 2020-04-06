"""
Problem: https://www.hackerrank.com/challenges/angry-professor/problem
"""

import os
def angryProfessor(k, a):
    attend_count = 0
    for i in a:
        if i<=0:
            attend_count+=1
    if attend_count<k:
        return "YES"
    else:
        return "NO"



if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        a = map(int, input().rstrip().split())

        result = angryProfessor(k, a)

        print(result)


"""
Input:
2
4 3
-1 -3 4 2
4 2
0 -1 2 1

Output:
YES
NO
"""