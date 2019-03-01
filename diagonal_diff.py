#!/bin/python3

# Time complexicity = O(n)

n = int(input().strip())
dSumLeft = 0
dSumRight = 0
for i in range(n):
    matrixRow = input().split()
    dSumLeft += int(matrixRow[i])
    dSumRight += int(matrixRow[-(i + 1)])
print(abs(dSumLeft-dSumRight))

