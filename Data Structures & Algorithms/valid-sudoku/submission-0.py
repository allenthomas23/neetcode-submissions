class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = set("123456789")
        for row in board:
            check = set()
            for num in row:
                if num in check:
                    return False
                elif num in valid:
                    check.add(num)
        for i in range(9):
            check = set()
            for j in range(9):
                num = board[j][i]
                if num in check:
                    return False
                elif num in valid:
                    check.add(num)
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                check = set()
                for r in range(box_row,box_row+3):
                    for c in range(box_col, box_col+3):
                        num = board[r][c]
                        if num in check:
                            return False
                        elif num in valid:
                            check.add(num)
        return True
            
        
        
            