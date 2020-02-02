def countSpecialElements(matrix):
    result = []
    row = len(matrix)
    col = len(matrix[0])
    for i in range(col):
        maxi = matrix[0][i]
        mini = matrix[0][i]
        for j in range(row):
            if matrix[j][i]>maxi:
                maxi = matrix[j][i]
            if matrix[j][i]<mini:
                mini = matrix[j][i]
        if maxi not in result:
            result.append(maxi)
        if mini not in result:
            result.append(mini)
    for i in range(row):
        maxi = mini =  matrix[i][0]
        # mini = matrix[0][i]
        for j in range(col):
            if matrix[i][j]>maxi:
                maxi = matrix[i][j]
            if matrix[i][j]<mini:
                mini = matrix[i][j]
        if maxi not in result:
            result.append(maxi)
        if mini not in result:
            result.append(mini)

    return len(result)

matrix = [[1,3,4],
          [5,2,9],
          [8,7,6]]
print(countSpecialElements(matrix))

