from ConnectFour.Board import Board
from ConnectFour.PlayerColorEnum import PlayerColorEnum
from ConnectFour.WinCalculator import WinCalculator
from collections import defaultdict

class ConnectFour:

    board: Board
    players: list[int]
    currentPlayer: int
    playerToColor: dict[int, PlayerColorEnum]
    rowToHeight: dict[int, int]
    isCompleted: bool
    wonPlayer: int | None

    def __init__(self, h: int, w:int):
        self.board = Board(h, w)
        self.players = []
        self.currentPlayer = 1
        self.rowToHeight = {}
        self.playerToColor = {}
        self.isCompleted = False
        self.wonPlayer = None
    

    def addPlayer(self, playerId: int):
        if playerId in self.playerToColor:
            return False

        if len(self.players) == 2:
            raise Exception("Not more players allowed")
        
        self.players.append(playerId)

        color = PlayerColorEnum['P' + str(len(self.players))].value

        self.playerToColor[playerId] = color

        return True
    
    def move(self, col: int, playerId: int) -> [bool, int]:
        if playerId not in self.playerToColor:
            raise Exception("Not a valid player")
        
        if col not in self.rowToHeight:
            self.rowToHeight[col] = -1
        
        if self.rowToHeight[col] + 1 == self.board.height or self.currentPlayer != playerId:
            raise Exception("Not a valid move")
        
        self.rowToHeight[col] += 1

        self.board.addToPosition(self.rowToHeight[col], col, self.playerToColor[playerId])

        won = WinCalculator.checkForWin(self.rowToHeight[col], col, self.playerToColor[playerId], self.board.matrix)

        if won == True:
            self.isCompleted = True
            self.wonPlayer = playerId

            return [True, playerId]
        
        isFull = self.checkBoardFull()

        if isFull == True:
            self.isCompleted = True

            return [True, None]
        
        self.currentPlayer = self.players[1] if self.currentPlayer == self.players[0] else self.players[0]
        
        return [False, None]
    
    def checkBoardFull(self) -> bool:
        h = self.board.height
        w = self.board.width

        for i in range(w):
            if i in self.rowToHeight and self.rowToHeight[i] != h-1:
                return False
        
        return True

        

