class Board:
    matrix: list[list]
    height: int
    width: int

    def __init__(self, h: int, w: int):
        self.matrix = [[None for _ in range(w)] for _ in range(h)]
        self.height = h
        self.width = w
    
    def addToPosition(self, row: int, col: int, data: int) -> bool:
        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            return False
        
        self.matrix[row][col] = data

        return True
    
    def getMatrix() -> list[int]:
        return self.matrix