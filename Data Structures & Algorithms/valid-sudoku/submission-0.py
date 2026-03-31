class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            d = {}
            for i in range(9):
                if row[i] != "." and row[i] in d:
                    return False
                else:
                    d[row[i]] = 1
        
        for i in range(len(board)):
            d = {}
            for j in range(len(board[0])):
                if board[j][i] != "." and board[j][i] in d:
                    return False
                else:
                    d[board[j][i]] = 1

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                seen = {}

                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):

                        val = board[r][c]

                        if val == ".":
                            continue

                        if val in seen:
                            return False

                        seen[val] = 1
        return True