
def minCost(cost,m,n,r,c):
    # Instead of following line, we can use int tc[m+1][n+1] or
    # dynamically allocate memoery to save space. The following
    # line is used to keep te program simple and make it working
    # on all compilers.
    tc = [[0 for x in range(c)] for x in range(r)]

    tc[0][0] = cost[0][0]

    # Initialize first column of total cost(tc) array
    for i in range(1, m + 1):
        tc[i][0] = tc[i - 1][0] + cost[i][0]

        # Initialize first row of tc array
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j - 1] + cost[0][j]

        # Construct rest of the tc array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min(tc[i - 1][j - 1], tc[i - 1][j], tc[i][j - 1]) + cost[i][j]

    return tc[m][n]

cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
r = len(cost)
c = len(cost[0])
print(minCost(cost, 2, 2,r, c))