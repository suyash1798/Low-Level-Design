Requirements

1. Players able to make move with col
2. Return or throw error on wrong move
3. Check for win after every move
4. Player should not able to play already completed game
5. Only 2 players allowed on each board
6. In case of board filled without any win mark it as completed

Wrong Move
- On already filled column
- Consecutive move from a single player
- outside of board
- already filled position

Win
- If consecutive 4 position filled by a single player (row, col , daig) then its a win
- If board fills without any win then its a Tie


Entities

1. ConnectFour
    - board
    - players (ids)
    - currentPlayer (id)
    - wonPlayer
    - completed
    - move(playerId, row, col)

2. WinCalculator
    - checkforwin(lr, lc)

3. Board
    - matrix
    - height
    - width
    - addToPosition(row, col)
    - getMatrix()

Flow

1. Move
    - Check its the current player or not
    - Check matrix if that position if filled or not
    - Check if one row below is filled or not
    - make move
    - check for win
    - if won mark completed

2. Check Win
    - get last pos filled
    - Check for position to left & right if four or position filled then return true
    - Check for position in same col in down direction
    - Check for daig & anti-daig for 4 for more position in any return true