def makeBoard(optional = None): # makeBoard([1, 0, 0], [0, 2, 0], [0, 0, 3]])
    board_size = 3
    if optional == None:
        board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    else:
        board = optional

    return board, board_size

board, board_size = makeBoard([[1, 0, 2], [0, 2, 0], [3, 0, 3]]) # Global variables

def printBoard():
    for i in range(board_size):
        print(str(board[i]).strip("[]"))

printBoard()


def checkSum():
    checkSumBool=False
    exceptedSum = board_size * (1 + board_size) // 2  

    for i in range(board_size):
        row_sum = sum(board[i])
        column_sum = sum([board[j][i] for j in range(board_size)])
    
    if exceptedSum == row_sum and exceptedSum == column_sum:
        checkSumBool = True

    return checkSumBool

checkSum()

"""

[expression function]
[board[j][i] for j in range(board_size)]
[board[0][i], board[1][i]...]

sum([board[0][i], board[1][i], board[2][i]])
board[0][i], board[1][i], board[2][i]
[[1, 0, 3], [1, 2, 0], [0, 0, 3]]


  1,  0,  0 i=0
  0,  2,  0 i=1
  0,  0,  3 i=2
j=0 j=1 j=2

"""
