from ConnectFour.ConnectFour import ConnectFour
import random


def printBoard():
    print('\n------Board Updated-------\n\n')
    for row in reversed(game.board.matrix):
        pr = [c if c != None else 'N' for c in row]
        print(str(pr)+'\n')



game = ConnectFour(7, 6)

game.addPlayer(1)
game.addPlayer(2)

while game.isCompleted == False:
    n = random.randint(0, 5)

    if n not in game.rowToHeight or game.rowToHeight[n] != 6:
        game.move(n, game.currentPlayer)
        printBoard()

        if game.isCompleted == True:
            print('Game Complete with Col ' + str(n) + ' ' + (str(game.wonPlayer) + ' Won the game') if game.wonPlayer != None else 'Its a Tie')
