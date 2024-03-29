class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        column = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in column[c] or board[r][c] in square[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                column[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True

            
             