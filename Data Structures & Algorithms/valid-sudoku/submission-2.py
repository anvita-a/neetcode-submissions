class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for i in range(9)]
        col = [[] for i in range(9)]
        grid = [[[] for i in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    if (board[i][j] in row[i]) or (board[i][j] in col[j]) or (board[i][j] in grid[i//3][j//3]):
                        return False
                    else:
                        row[i].append(board[i][j])
                        col[j].append(board[i][j])
                        grid[i//3][j//3].append(board[i][j])
        return True
        
        