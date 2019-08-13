square = [['B','A','L','L'],
          ['A','R','E','A'],
          ['L','E','A','D'],
          ['L','A','D','Y']]

row = len(square)
col = len(square[0])
def find_sqaure(row,col):
    for i in range(row):
        for j in range(col):
            if square[i][j] == square[j][i]:
                square[i][j] = square[j][i]
            else:
                print(False)
    return(square)

print(find_sqaure(row,col))





