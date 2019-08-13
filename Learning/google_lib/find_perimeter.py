mat = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
row = len(mat)
col = len(mat[0])

def numneighbours(mat,i,j):
    count = 0
    if i>0 and mat[i-1][j]:
        count+=1
    if j>0 and mat[i][j-1]:
        count+=1
    if i<row-1 and mat[i+1][j]:
        count+=1
    if j<col-1 and mat[i][j+1]:
        count+=1
    return count

def perimetr(mat):
    p = 0
    for i in range(row):
        for j in range(col):
            if mat[i][j]:
                p +=(4-numneighbours(mat,i,j))

    return p

print(perimetr(mat))