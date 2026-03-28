class WinCalculator:
    DIRS = [
            [[-1, 0], [1, 0]],
            [[0, -1], [0, 1]],
            [[-1, -1], [1, 1]],
            [[1, -1], [-1, 1]]
    ]

    def checkForWin(row, col, color, board):

        for dir in WinCalculator.DIRS:
            count = 1
            for r, c in dir:
                nr, nc = row + r, col + c

                while nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]) and board[nr][nc] == color:
                    count += 1

                    if count == 4:
                        return True
                    
                    nr, nc = nr + r, nc + c
        
        return False