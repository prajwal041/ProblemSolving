class Graph:

    def __init__(self, row, col, g):
        self.row = row
        self.col = col
        self.graph = g

        # A function to check if a given cell

    # (row, col) can be included in DFS
    def isSafe(self, i, j, visited):
        # row number is in range, column number
        # is in range and value is 1
        # and not yet visited
        return (i >= 0 and i < self.row and
                j >= 0 and j < self.col and
                not visited[i][j] and self.graph[i][j])

        # A utility function to do DFS for a 2D

    # boolean matrix. It only considers
    # the 8 neighbours as adjacent vertices
    def DFS(self, i, j, visited):

        # These arrays are used to get row and
        # column numbers of 8 neighbours
        # of a given cell
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]

        # Mark this cell as visited

        visited[i][j] = True

    # Recur for all connected neighbours
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)

            # The main function that returns


# count of islands in a given boolean
# 2D matrix
    def countIslands(self):
    # Make a bool array to mark visited cells.
    # Initially all cells are unvisited
        visited = [[False for j in range(self.col)] for i in range(self.row)]

    # Initialize count as 0 and travese
    # through the all cells of
    # given matrix
        count = 0
        for i in range(self.row):
            for j in range(self.col):
            # If a cell with value 1 is not visited yet,
            # then new island found
                if visited[i][j] == False and self.graph[i][j] == 1:
                # Visit all cells in this island
                # and increment island count
                    self.DFS(i, j, visited)
                    count += 1
        return count

graph=[[1,1,0,0,0],
      [0,1,0,0,1],
      [1,0,0,1,1],
      [0,0,0,0,0],
      [1,0,1,0,1]]

row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)

print("Number of islands is:")
print(g.countIslands())

# import collections
# class Solution(object):
#     def is_valid(self, grid, r, c):
#         m, n = len(grid), len(grid[0])
#         if r < 0 or c < 0 or r >= m or c >= n:
#             return False
#         return True
#
#     def numIslandsDFS(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         if not grid or not grid[0]:
#             return 0
#
#         m, n = len(grid), len(grid[0])
#         count = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     self.dfs(grid, i, j)
#                     count += 1
#         return count
#
#     def dfs(self, grid, r, c):
#         grid[r][c] = '0'
#         directions = [(0,1), (0,-1), (-1,0), (1,0)]
#         for d in directions:
#             nr, nc = r + d[0], c + d[1]
#             if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1':
#                 self.dfs(grid, nr, nc)
#
#     def numIslandsBFS(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         if not grid or not grid[0]:
#             return 0
#
#         m, n = len(grid), len(grid[0])
#         count = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == '1':
#                     self.bfs(grid, i, j)
#                     count += 1
#         return count
#
#     def bfs(self, grid, r, c):
#         queue = collections.deque()
#         queue.append((r, c))
#         grid[r][c] = '0'
#         while queue:
#             directions = [(0,1), (0,-1), (-1,0), (1,0)]
#             r, c = queue.popleft()
#             for d in directions:
#                 nr, nc = r + d[0], c + d[1]
#                 if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1':
#                     queue.append((nr, nc))
#                     grid[nr][nc] = '0'

