def solution(m):
    if all(sum(row) == 1 for row in m):
        # Check columns
        return all(sum(col) == 1 for col in zip(*m))
    return False


m = int(input())
n = int(input())

mat = []
for j in range(n):
    mat.append(int(input()))

matrix = []
for i in range(len(mat)):
    matrix.append([int(numeric_string) for numeric_string in list(bin(int(mat[i]))[2:].zfill(n))])

val = solution(matrix)
if val == False:
    print('0')
else:
    print('1')


'''
Your output (clipped to one character)
0
'''