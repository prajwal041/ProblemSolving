def findmatch(mat,pat,i,j,row,col,level):
    l = len(pat)
    if level==l:
        return True
    if i<0 or j<0 or i>=row or j>=col:
        return False
    if mat[i][j]==pat[level]:
        t = mat[i][j]
        mat[i][j]="#"
        res = (findmatch(mat,pat,i-1,j,row,col,level+1)|
               findmatch(mat,pat,i+1,j,row,col,level+1)|
               findmatch(mat,pat,i,j-1,row,col,level+1)|
               findmatch(mat,pat,i,j+1,row,col,level+1))
        mat[i][j]=t
        return res
    else:
        return False

def checkmatch(mat,pat,row,col):
    l = len(pat)
    if l>row*col:
        return False
    for i in range(row):
        for j in range(col):
            if mat[i][j]==pat[0]:
                if findmatch(mat,pat,i,j,row,col,0):
                    return True
    return False

mat =[['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']]
row = len(mat)
col = len(mat[0])
pat="ABCB"
print(checkmatch(mat,pat,row,col))