# Thomas Rooney Roone194
# I understand this is a graded, individual examination that may not be
# discussed with anyone.  I also understand that obtaining solutions or
# partial solutions from outside sources, or discussing
# any aspect of the examination with anyone will result in failing the course.
# I further certify that this program represents my own work and that none of
# it was obtained from any source other than material presented as part of the
# course.

import turtle
import random

#stamps a green square
def zeroStamp(x, y):
    x = x + .5
    y = y + .5
    turtle.getscreen()
    turtle.delay(0)
    turtle.speed(0)
    turtle.tracer(0, 0)
    turtle.ht()
    turtle.pu()
    turtle.goto(x, y)
    turtle.color('green')
    turtle.shape('square')
    turtle.shapesize(2.75, 2.75)
    turtle.stamp()

#stamps a black circle corresponding to the users game pieces
def oneStamp(x, y):
    x = x + .5
    y = y + .5
    turtle.getscreen()
    turtle.delay(0)
    turtle.speed(0)
    turtle.tracer(0, 0)
    turtle.ht()
    turtle.pu()
    turtle.goto(x, y)
    turtle.color('black')
    turtle.shape('circle')
    turtle.shapesize(2.75, 2.75)
    turtle.stamp()

#stamps a white circle corresponding to the computers game pieces
def twoStamp(x, y):
    x = x + .5
    y = y + .5
    turtle.getscreen()
    turtle.delay(0)
    turtle.speed(0)
    turtle.tracer(0, 0)
    turtle.ht()
    turtle.pu()
    turtle.goto(x, y)
    turtle.color('white')
    turtle.shape('circle')
    turtle.shapesize(2.75, 2.75)
    turtle.stamp()

#converts the user input into the correct matrix location
def convertRow(row):
    if row == 0:
        row += 7
    elif row == 1:
        row += 5
    elif row == 2:
        row += 3
    elif row == 3:
        row += 1
    elif row == 4:
        row -= 1
    elif row == 5:
        row -= 3
    elif row == 6:
        row -= 5
    else:
        row -= 7
    return(row)

#initalizes board with a 8 x 8 grid of all zeros, i.e. green squares
#return 2 dimensional list that acts as the board matrix
def initialBoard():
    initialBoard = [[0 for x in range(8)] for y in range(8)]
    return(initialBoard)

#inputs a nested list
#outputs initial positions of white and black pieces
def initializeBoard(board):
    updatedBoard = board
    updatedBoard[4][3] = 2
    updatedBoard[4][4] = 1
    updatedBoard[3][3] = 1
    updatedBoard[3][4] = 2
    return(updatedBoard)

#updates the board by scanning the matrix and depending on 0,1,2
#and stamps the corresponding piece
def update(board):
    turtle.getscreen()
    turtle.delay(0)
    turtle.speed(0)
    turtle.tracer(0, 0)
    for r in range(8):
        for c in range(8):
            if board[r][c] == 1:
                oneStamp(r, c)
            elif board[r][c] == 2:
                twoStamp(r, c)
            else:
                zeroStamp(r, c)

#Draw the numbers around the edge
def drawCoordinateSystem():
    turtle.getscreen()
    turtle.delay(0)
    turtle.speed(0)
    turtle.tracer(0, 0)
    turtle.ht()
    turtle.color('black')
    turtle.penup()
    turtle.goto(-.25, .35)
    turtle.setheading(90)
    count = 7
    while count >= 0:
        turtle.write(count, align = 'center', font = (15))
        turtle.forward(1)
        count -= 1
    turtle.goto(.5, 8.25)
    turtle.setheading(0)
    count = 0
    while count <= 7:
        turtle.write(count, align = 'center', font = (15))
        turtle.forward(1)
        count += 1
    turtle.update()

#inputs the matrix, the row and column of the intended move, and the number of
#color
#outputs the count of how many opponent neighbors the row, column has
#and where positionally the opponent is located
def opponentCheckNeighbors(board, row, column, color):
    up = False
    right = False
    left = False
    down = False
    upRight = False
    upLeft = False
    downRight = False
    downLeft = False
    count = 0
    if row == 0 and column == 0:
        if board[row][column + 1] != 0 and board[row][column + 1] != color:
            count += 1
            up = True
        if board[row + 1][column + 1] != 0 and board[row + 1][column + 1] != color:
            count += 1
            upRight = True
        if board[row + 1][column] != 0 and board[row + 1][column] != color:
            count += 1
            left = True
    elif row == 0 and column == 7:
        if board[row][column - 1] != 0 and board[row][column - 1] != color:
            count += 1
            down = True
        if board[row + 1][column - 1] != 0 and board[row + 1][column - 1] != color:
            count += 1
            downRight = True
        if board[row + 1][column] != 0 and board[row + 1][column] != color:
            count += 1
            right = True
    elif row == 7 and column == 7:
        if board[row - 1][column] != 0 and board[row - 1][column] != color:
            count += 1
            left = True
        if board[row - 1][column - 1] != 0 and board[row - 1][column - 1] != color:
            count += 1
            downLeft = True
        if board[row][column - 1] != 0 and board[row][column - 1] != color:
            count += 1
            down = True
    elif row == 7 and column == 0:
        if board[row - 1][column] != 0 and board[row - 1][column] != color:
            count += 1
            left = True
        if board[row - 1][column + 1] != 0 and board[row - 1][column + 1] != color:
            count += 1
            upLeft = True
        if board[row][column + 1] != 0 and board[row][column + 1] != color:
            count += 1
            up = True
    elif row == 0:
        if board[row][column + 1] != 0 and board[row][column + 1] != color:
            count += 1
            up = True
        if board[row + 1][column + 1] != 0 and board[row + 1][column + 1] != color:
            count += 1
            upRight = True
        if board[row + 1][column] != 0 and board[row + 1][column] != color:
            count += 1
            right = True
        if board[row + 1][column - 1] != 0 and board[row + 1][column - 1] != color:
            count += 1
            downRight = True
        if board[row][column - 1] != 0 and board[row][column - 1] != color:
            count += 1
            down = True
    elif column == 7:
        if board[row - 1][column] != 0 and board[row - 1][column] != color:
            count += 1
            left = True
        if board[row - 1][column - 1] != 0 and board[row - 1][column - 1] != color:
            count += 1
            downLeft = True
        if board[row + 1][column] != 0 and board[row + 1][column] != color:
            count += 1
            right = True
        if board[row + 1][column - 1] != 0 and board[row + 1][column - 1] != color:
            count += 1
            downRight = True
        if board[row][column - 1] != 0 and board[row][column - 1] != color:
            count += 1
            down = True
    elif row == 7:
        if board[row - 1][column - 1] != 0 and board[row - 1][column - 1] != color:
            count += 1
            downLeft = True
        if board[row - 1][column] != 0 and board[row - 1][column] != color:
            count += 1
            left = True
        if board[row - 1][column + 1] != 0 and board[row - 1][column + 1] != color:
            count += 1
            upLeft = True
        if board[row][column + 1] != 0 and board[row][column + 1] != color:
            count += 1
            up = True
        if board[row][column - 1] != 0 and board[row][column - 1] != color:
            count += 1
            down = True
    elif column == 0:
        if board[row - 1][column] != 0 and board[row - 1][column] != color:
            count += 1
            left = True
        if board[row - 1][column + 1] != 0 and board[row - 1][column + 1] != color:
            count += 1
            upLeft = True
        if board[row][column + 1] != 0 and board[row][column + 1] != color:
            count += 1
            up = True
        if board[row + 1][column + 1] != 0 and board[row + 1][column + 1] != color:
            count += 1
            upRight = True
        if board[row + 1][column] != 0 and board[row + 1][column] != color:
            count += 1
            right = True
    else:
        if board[row - 1][column - 1] != 0 and board[row - 1][column - 1] != color:
            count += 1
            downLeft = True
        if board[row - 1][column] != 0 and board[row - 1][column] != color:
            count += 1
            left = True
        if board[row - 1][column + 1] != 0 and board[row - 1][column + 1] != color:
            count += 1
            upLeft = True
        if board[row][column + 1] != 0 and board[row][column + 1] != color:
            count += 1
            up = True
        if board[row + 1][column + 1] != 0 and board[row + 1][column + 1] != color:
            count += 1
            upRight = True
        if board[row + 1][column] != 0 and board[row + 1][column] != color:
            count += 1
            right = True
        if board[row + 1][column - 1] != 0 and board[row + 1][column - 1] != color:
            count += 1
            downRight = True
        if board[row][column - 1] != 0 and board[row][column - 1] != color:
            count += 1
            down = True
    return(count, up, down, left, right, upRight, upLeft, downLeft, downRight)

#recursive function that checks if a move to the right is valid
def moveValidityRight(board, row, column, color):
    if board[row][column] == color:
        return(True)
    else:
        if row == 7:
            if board[row][column] != color and board[row][column] != 0:
                return(False)
        elif row < 7:
            if board[row][column] != color and board[row][column] != 0:
                return(moveValidityRight(board, row + 1, column, color))
        else:
            return(False)

#recursive function that flips the correct pieces to the right
#after a valid move has been made
def flipRight(board, row, column, color):
    if board[row][column] == color:
        return(board)
    else:
        if board[row][column] != color and board[row][column] != 0:
            board[row][column] = color
            update(board)
            return(flipRight(board, row + 1, column, color))

#recursive function that checks if a move to the left is valid
def moveValidityLeft(board, row, column, color):
    if board[row][column] == color:
        return(True)
    else:
        if row == 0:
            if board[row][column] != color and board[row][column] != 0:
                return(False)
        if row > 0:
            if board[row][column] != color and board[row][column] != 0:
                return(moveValidityLeft(board, row - 1, column, color))
        else:
            return(False)

#recursive function that flips the correct pieces to the left
#after a valid move has been made
def flipLeft(board, row, column, color):
    if board[row][column] == color:
        return(board)
    else:
        if board[row][column] != color and board[row][column] != 0:
            board[row][column] = color
            return(flipLeft(board, row - 1, column, color))

#recursive function that checks if a move up is valid
def moveValidityUp(board, row, column, color):
    if board[row][column] == color:
        return(True)
    else:
        if column == 7:
            if board[row][column] != color and board[row][column] != 0:
                return(False)
        elif column < 7:
            if board[row][column] != color and board[row][column] != 0:
                return(moveValidityUp(board, row, column + 1, color))
        else:
            return(False)

#recursive function that flips the correct pieces upward
#after a valid move has been made
def flipUp(board, row, column, color):
    if board[row][column] == color:
        return(board)
    else:
        if board[row][column] != color and board[row][column] != 0:
            board[row][column] = color
            update(board)
            return(flipUp(board, row, column + 1, color))

#recursive function that checks if a move down is valid
def moveValidityDown(board, row, column, color):
    if board[row][column] == color:
        return(True)
    else:
        if column == 0:
            if board[row][column] != color and board[row][column] != 0:
                return(False)
        elif column > 0:
            if board[row][column] != color and board[row][column] != 0:
                return(moveValidityDown(board, row, column - 1, color))
        else:
            return(False)

#recursive function that flips the correct pieces downward
#after a valid move has been made
def flipDown(board, row, column, color):
    if board[row][column] == color:
        return(board)
    else:
        if board[row][column] != color and board[row][column] != 0:
            board[row][column] = color
            update(board)
            return(flipDown(board, row, column - 1, color))

#recursive function that checks if a move up and to the right is valid
def moveValidityUpRight(board, row, column, color):
    if board[row][column] == color:
        return(True)
    else:
        if row == 7 or column == 7:
            if board[row][column] != color and board[row][column] != 0:
                return(False)
        elif row < 7 and column < 7:
            if board[row][column] != color and board[row][column] != 0:
                return(moveValidityUpRight(board, row + 1, column + 1, color))
        else:
            return(False)

#recursive function that flips the correct pieces up and to the right
#after a valid move has been made
def flipUpRight(board, row, column, color):
    if board[row][column] == color:
        return(board)
    else:
        if board[row][column] != color and board[row][column] != 0:
            board[row][column] = color
            update(board)
            return(flipUpRight(board, row + 1, column + 1, color))

#recursive function that checks if a move up and to the left is valid
def moveValidityUpLeft(board, row, column, color):
    if board[row][column] == color:
        return(True)
    else:
        if row == 0 or column == 7:
            if board[row][column] != color and board[row][column] != 0:
                return(False)
        elif row > 0 and column < 7:
            if board[row][column] != color and board[row][column] != 0:
                return(moveValidityUpLeft(board, row - 1, column + 1, color))
        else:
            return(False)

#recursive function that flips the correct pieces up and to the left
#after a valid move has been made
def flipUpLeft(board, row, column, color):
    if board[row][column] == color:
        return(board)
    else:
        if board[row][column] != color and board[row][column] != 0:
            board[row][column] = color
            update(board)
            return(flipUpLeft(board, row - 1, column + 1, color))

#recursive function that checks if a move down and to the right is valid
def moveValidityDownRight(board, row, column, color):
    if board[row][column] == color:
        return(True)
    else:
        if row == 7 or column == 0:
            if board[row][column] != color and board[row][column] != 0:
                return(False)
        elif row < 7 and column > 0:
            if board[row][column] != color and board[row][column] != 0:
                return(moveValidityDownRight(board, row + 1, column - 1, color))
        else:
            return(False)

#recursive function that flips the correct pieces down and to the right
#after a valid move has been made
def flipDownRight(board, row, column, color):
    if board[row][column] == color:
        return(board)
    else:
        if board[row][column] != color and board[row][column] != 0:
            board[row][column] = color
            update(board)
            return(flipDownRight(board, row + 1, column - 1, color))

#recursive function that checks if a move down and to the left is valid
def moveValidityDownLeft(board, row, column, color):
    if board[row][column] == color:
        return(True)
    else:
        if row == 0 or column == 0:
            if board[row][column] != color and board[row][column] != 0:
                return(False)
        elif row > 0 and column > 0:
            if board[row][column] != color and board[row][column] != 0:
                return(moveValidityDownLeft(board, row - 1, column - 1, color))
        else:
            return(False)

#recursive function that flips the correct pieces down and to the left
#after a valid move has been made
def flipDownLeft(board, row, column, color):
    if board[row][column] == color:
        return(board)
    else:
        if board[row][column] != color and board[row][column] != 0:
            board[row][column] = color
            update(board)
            return(flipDownLeft(board, row - 1, column - 1, color))

#inputs a given board matrix, a row, a column, and a color
#outputs a bool signifying if it is a valid move or not
def isValidMove(board, row, column, color):
    if board[row][column] == 0:
        opponentNeighbors = opponentCheckNeighbors(board, row, column, color)
        rowPlusOne = row + 1
        rowMinusOne = row - 1
        columnPlusOne = column + 1
        columnMinusOne = column - 1
        if opponentNeighbors[0] > 0:
            count = 0
            if opponentNeighbors[1]:
                if moveValidityUp(board, row, columnPlusOne, color):
                    count += 1
            if opponentNeighbors[2]:
                if moveValidityDown(board, row, columnMinusOne, color):
                    count += 1
            if opponentNeighbors[3]:
                if moveValidityLeft(board, rowMinusOne, column, color):
                    count += 1
            if opponentNeighbors[4]:
                if moveValidityRight(board, rowPlusOne, column, color):
                    count += 1
            if opponentNeighbors[5]:
                if moveValidityUpRight(board, rowPlusOne, columnPlusOne, color):
                    count += 1
            if opponentNeighbors[6]:
                if moveValidityUpLeft(board, rowMinusOne, columnPlusOne, color):
                    count += 1
            if opponentNeighbors[7]:
                if moveValidityDownLeft(board, rowMinusOne, columnMinusOne, color):
                    count += 1
            if opponentNeighbors[8]:
                if moveValidityDownRight(board, rowPlusOne, columnMinusOne, color):
                    count += 1
            if count > 0:
                return(True)
            else:
                return(False)
        else:
            return(False)
    else:
        return(False)

#inputs the board matrix and the color number
#outputs a list of all the possible valid moves
def getValidMoves(board, color):
    listOfValidMoves = []
    for r in range(8):
        for c in range(8):
            if isValidMove(board, r, c, color):
                listOfValidMoves.append([r,c])
    return(listOfValidMoves)

#Checks to see all available moves for computer
#Randomly picks a move from available moves
#updates the board accordingly
#inputs the board matrix
#outputs the updated board matrix
def selectNextPlay(board):
    validMoves = getValidMoves(board, 2)
    randMove = random.randint(0, len(validMoves) - 1)
    theMove = validMoves[randMove]
    checkNeighbors = opponentCheckNeighbors(board, theMove[0], theMove[1], 2)
    if checkNeighbors[1]:
        if moveValidityUp(board, theMove[0], theMove[1] + 1, 2):
            flipUp(board, theMove[0], theMove[1] + 1, 2)
    if checkNeighbors[2]:
        if moveValidityDown(board, theMove[0], theMove[1] - 1, 2):
            flipDown(board, theMove[0], theMove[1] - 1, 2)
    if checkNeighbors[3]:
        if moveValidityLeft(board, theMove[0] - 1, theMove[1], 2):
            flipLeft(board, theMove[0] - 1, theMove[1], 2)
    if checkNeighbors[4]:
        if moveValidityRight(board, theMove[0] + 1, theMove[1], 2):
            flipRight(board, theMove[0] + 1, theMove[1], 2)
    if checkNeighbors[5]:
        if moveValidityUpRight(board, theMove[0] + 1, theMove[1] + 1, 2):
            flipUpRight(board, theMove[0] + 1, theMove[1] + 1, 2)
    if checkNeighbors[6]:
        if moveValidityUpLeft(board, theMove[0] - 1, theMove[1] + 1, 2):
            flipUpLeft(board, theMove[0] - 1, theMove[1] + 1, 2)
    if checkNeighbors[7]:
        if moveValidityDownLeft(board, theMove[0] - 1, theMove[1] - 1, 2):
            flipDownLeft(board, theMove[0] - 1, theMove[1] - 1, 2)
    if checkNeighbors[8]:
        if moveValidityDownRight(board, theMove[0] + 1, theMove[1] - 1, 2):
            flipDownRight(board, theMove[0] + 1, theMove[1] - 1, 2)
    board[theMove[0]][theMove[1]] = 2
    update(board)
    return(board)

#prompts user to input a row,column
#checks if the move is valid
#updates board accordingly if move is valid
#inputs board matrix
#outputs updated board matrix
def getPlayerInput(board):
    playerInput = turtle.textinput('', 'Enter row,column: ')
    playerInputList = playerInput.split(',')
    playerInputList = [int(playerInputList[1]), convertRow(int(playerInputList[0]))]
    while playerInputList not in getValidMoves(board, 1):
        playerInput = turtle.textinput('', 'Invalid move, Enter row,column: ')
        playerInputList = playerInput.split(',')
        playerInputList = [int(playerInputList[1]), convertRow(int(playerInputList[0]))]
    if isValidMove(board, playerInputList[0], playerInputList[1], 1):
        checkNeighbors = opponentCheckNeighbors(board, playerInputList[0], playerInputList[1], 1)
        if checkNeighbors[1]:
            if moveValidityUp(board, playerInputList[0], playerInputList[1] + 1, 1):
                flipUp(board, playerInputList[0], playerInputList[1] + 1, 1)
        if checkNeighbors[2]:
            if moveValidityDown(board, playerInputList[0], playerInputList[1] - 1, 1):
                flipDown(board, playerInputList[0], playerInputList[1] - 1, 1)
        if checkNeighbors[3]:
            if moveValidityLeft(board, playerInputList[0] - 1, playerInputList[1], 1):
                flipLeft(board, playerInputList[0] - 1, playerInputList[1], 1)
        if checkNeighbors[4]:
            if moveValidityRight(board, playerInputList[0] + 1, playerInputList[1], 1):
                flipRight(board, playerInputList[0] + 1 , playerInputList[1], 1)
        if checkNeighbors[5]:
            if moveValidityUpRight(board, playerInputList[0] + 1, playerInputList[1] + 1, 1):
                flipUpRight(board, playerInputList[0] + 1, playerInputList[1] + 1, 1)
        if checkNeighbors[6]:
            if moveValidityUpLeft(board, playerInputList[0] - 1, playerInputList[1] + 1, 1):
                flipUpLeft(board, playerInputList[0] - 1, playerInputList[1] + 1, 1)
        if checkNeighbors[7]:
            if moveValidityDownLeft(board, playerInputList[0] - 1, playerInputList[1] - 1, 1):
                flipDownLeft(board, playerInputList[0] - 1, playerInputList[1] - 1, 1)
        if checkNeighbors[8]:
            if moveValidityDownRight(board, playerInputList[0] + 1, playerInputList[1] - 1, 1):
                flipDownRight(board, playerInputList[0] + 1, playerInputList[1] - 1, 1)
        board[playerInputList[0]][playerInputList[1]] = 1
        update(board)
    return(board)

#inputs color string, count of black circles and whites circles
#displays the winner on the board and the magnitudes of the black, white pieces
def winner(color, blackCount, whiteCount):
    turtle.ht()
    turtle.pu()
    turtle.goto(4, 4)
    turtle.color('red')
    turtle.write(color, True, align = 'center', font = ('Arial',100,'normal'))
    turtle.goto(4, 2)
    turtle.write('Black: '+ blackCount + ' White: '+ whiteCount, True, align = 'center', font = ('Arial',50,'normal'))

def main():
    turtle.setworldcoordinates(-1, -1, 9, 9)
    drawCoordinateSystem()
    update(initialBoard())
    update(initializeBoard(initialBoard()))
    board = initializeBoard(initialBoard())
    while len(getValidMoves(board, 1)) > 0 or len(getValidMoves(board, 2)) > 0:
        if len(getValidMoves(board, 1)) > 0:
            board = getPlayerInput(board)
            update(board)
        if len(getValidMoves(board, 2)) > 0:
            board = selectNextPlay(board)
            update(board)
    oneCount = 0
    twoCount = 0
    black = 'Black Wins!'
    white = 'White Wins!'
    catGame = 'Tie Game!'
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                oneCount += 1
            elif board[i][j] == 2:
                twoCount += 1
    if oneCount > twoCount:
        winner(black, str(oneCount), str(twoCount))
    elif twoCount > oneCount:
        winner(white, str(oneCount), str(twoCount))
    else:
        winner(catGame, str(oneCount), str(twoCount))

if __name__ == '__main__':
    main()
