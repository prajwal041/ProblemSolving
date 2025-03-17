class Solution:
    def exist(self, board, word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                print(board[row][col])

    def dfs(self, row, col, word, board):
        if len(word) == 0:
            return True
        if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col]!= word[0]):
            return False
        result = False
        board[row][col] = '*'



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
s = Solution()
print(s.exist(board, word))