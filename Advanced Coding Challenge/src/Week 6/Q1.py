'''
1. Tic-tac-toe
Problem Description
You are going to implement the mini-game 3x3 Tic-tac-toe using Python script.

Game Description
Tic-tac-toe is played on a 3 x 3 grid by two players, who alternately place the marks X and O in one of the nine spaces in the grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.

More information about the game: Tic-tac-toe - Wikipedia

Coding Requirement
The game board is represented by numbers from 1 - 9. The first row is starting from 1 to 3, and so on so forth. You may consider the initial game board like this:

| 1 || 2 || 3 |
| 4 || 5 || 6 |
| 7 || 8 || 9 |
Player X would always take the first move. If he or she decided to place X in position 6, the game board would therefore be:

| 1 || 2 || 3 |
| 4 || 5 || X |
| 7 || 8 || 9 |
Note: you may need to print out the board each time before the user input and also when the game comes to an end.

To get the user's input, prompts might be given to users: when it's Player X's turn, the prompt should be X:  ; for Player O, it should be O:  .

The valid input by the users should be integers from 1 - 9 which represent the position where they take as their move. If the input is invalid, send the message Error: invalid input . If the position is already occupied, send the message Error: N/A position . And then ask the user for input again.

If Player X wins, print out Player X wins . If Player O wins, print out Player O wins . However, if the positions of the board are all occupied and no one is winning, you may print out Tie .

Sample Input&Output

Bold text is the input by the user

Case 1:

| 1 || 2 || 3 |
| 4 || 5 || 6 |
| 7 || 8 || 9 |
X: 1
| X || 2 || 3 |
| 4 || 5 || 6 |
| 7 || 8 || 9 |
O: abc
Error: invalid input
| X || 2 || 3 |
| 4 || 5 || 6 |
| 7 || 8 || 9 |
O: 5
| X || 2 || 3 |
| 4 || O || 6 |
| 7 || 8 || 9 |
X: 5
Error: N/A position
| X || 2 || 3 |
| 4 || O || 6 |
| 7 || 8 || 9 |
X: 3
| X || 2 || X |
| 4 || O || 6 |
| 7 || 8 || 9 |
O: 6
| X || 2 || X |
| 4 || O || O |
| 7 || 8 || 9 |
X: 7
| X || 2 || X |
| 4 || O || O |
| X || 8 || 9 |
O: 4
| X || 2 || X |
| O || O || O |
| X || 8 || 9 |
Player O wins

Case 2:

| 1 || 2 || 3 |
| 4 || 5 || 6 |
| 7 || 8 || 9 |
X: 1
| X || 2 || 3 |
| 4 || 5 || 6 |
| 7 || 8 || 9 |
O: 2
| X || O || 3 |
| 4 || 5 || 6 |
| 7 || 8 || 9 |
X: 6
| X || O || 3 |
| 4 || 5 || X |
| 7 || 8 || 9 |
O: 5
| X || O || 3 |
| 4 || O || X |
| 7 || 8 || 9 |
X: 7
| X || O || 3 |
| 4 || O || X |
| X || 8 || 9 |
O: 4
| X || O || 3 |
| O || O || X |
| X || 8 || 9 |
X: 8
| X || O || 3 |
| O || O || X |
| X || X || 9 |
O: 9
| X || O || 3 |
| O || O || X |
| X || X || O |
X: 3
| X || O || X |
| O || O || X |
| X || X || O |
Tie
'''
# Solution:
line1 = [1, 2, 3]
line2 = [4, 5 ,6]
line3 = [7, 8, 9]

chessTable = [line1,line2,line3]

size = 3

def printBoard():
    printLine(line1)
    printLine(line2)
    printLine(line3)

def printLine(line):
    for i in range(len(line)):

        if i < len(line)-1:
            print("|",line[i],"|", end="")
        else:
            print("|",line[i],"|")

# Turn functions for X and O
def xTurn():
    position = int(input("X: "))
    if(isRepeat(position)):
        print("Error: N/A position")
        printBoard()
        xTurn()
    elif(type(position) != int or position > 9 or position < 1 ):
        print("Error: invalid input")
        printBoard()
        xTurn()
    else:
        if(position >= 1 and position <= 3):
            line1.remove(position)
            line1.insert(position-1,"X")
        if(position >= 4 and position <= 6):
            line2.remove(position)
            line2.insert(position-4,"X")
        if(position >= 7 and position <= 9):
            line3.remove(position)
            line3.insert(position-7,"X")

def oTurn():
    position = int(input("O: "))
    if(isRepeat(position)):
        print("Error: N/A position")
        printBoard()
        oTurn()
    elif(type(position) != int or position > 9 or position < 1 ):
        print("Error: invalid input")
        printBoard()
        oTurn()
    else:
        if(position >= 1 and position <= 3):
            line1.remove(position)
            line1.insert(position-1,"O")
        if(position >= 4 and position <= 6):
            line2.remove(position)
            line2.insert(position-4,"O")
        if(position >= 7 and position <= 9):
            line3.remove(position)
            line3.insert(position-7,"O")

def isRepeat(position):
    if(position >= 1 and position <= 3):
        if line1[position-1] == "O" or line1[position-1] == "X":
            return True
        else:
            return False
    if(position >= 4 and position <= 6):
        if line2[position-4] == "O" or line2[position-4] == "X":
            return True
        else:
            return False
    if(position >= 7 and position <= 9):
        if line3[position-7] == "O" or line3[position-7] == "X":
            return True
        else:
            return False

def checkStatus(side):
    for i in range(0,size):
        count = 0
        for j in range(0,size):
            if chessTable[i][j] == side:
                count += 1
            else:
                count = 0
            if count == size:
                return True

    for i in range(0,size):
        count = 0
        for j in range(0,size):
            if chessTable[j][i] == side:
                count += 1
            else:
                count = 0
            if count == size:
                return True
    
    if chessTable[0][0] == side:
        count = 0
        for i in range(0,size):
            if chessTable[i][i] == side:
                count += 1
            else:
                count = 0
            if count == size:
                return True
    
    if chessTable[0][size-1] == side:
        count = 0
        for i in range(0,size):
            if chessTable[i][size-i-1] == side:
                count += 1
            else:
                count = 0
            if count == size:
                return True
    
    return False

def isFull():

    for i in range(3):
        for j in range(3):
            if str(chessTable[i][j]).isdigit():
                return False
    
    return True

printBoard()

while(True):
    xTurn()
    printBoard()
    if(checkStatus("X")):
        print("Player X wins")
        break
    if(isFull()):
        print("Tie")
        break
    oTurn()
    printBoard()
    if(checkStatus("O")):
        print("Player O wins")
        break
    if(isFull()):
        print("Tie")
        break