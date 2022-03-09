from b import board, board_width, board_length, print_board
from random import randint

# variable
bomb_count = 5
around_bomb_square = [
    (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)    
]

def plant_bombs():
    def cover_bomb_squre_with_one(bomb_x, bomb_y):
        for item in around_bomb_square:
            diff_x, diff_y = item
            cell_x = bomb_x + diff_x
            cell_y = bomb_y + diff_y
            if 0 <= cell_x < board_width and 0 <= cell_y < board_length and board[cell_y][cell_x] != 2:
                board[cell_y][cell_x] = 1
            
    for _ in range(bomb_count):
        bomb_x = randint(0, board_width - 1)
        bomb_y = randint(0, board_length - 1)
        board[bomb_y][bomb_x] = 2
        cover_bomb_squre_with_one(bomb_x, bomb_y)
        # print(bomb_x, bomb_y)

import random


class boardSpot(object):
    value = 0
    selected = False
    mine = False

    def __init__(self):
        self.selected = False

    def __str__(self):
        return str(boardSpot.value)

    def isMine(self):
        if boardSpot.value == -1:
            return True
        return False


class boardClass(object):
    def __init__(self, m_boardSize, m_numMines):
        self.board = [[boardSpot() for i in range(m_boardSize)] for j in range(m_boardSize)]
        self.boardSize = m_boardSize
        self.numMines = m_numMines
        self.selectableSpots = m_boardSize * m_boardSize - m_numMines
        i = 0
        while i < m_numMines:
            x = random.randint(0, self.boardSize-1)
            y = random.randint(0, self.boardSize-1)
            if not self.board[x][y].mine:
                self.addMine(x, y)
                i += 1
            else:
                i -= 1

    def __str__(self):
        returnString = " "
        divider = "\n---"

        for i in range(0, self.boardSize):
            returnString += " | " + str(i)
            divider += "----"
        divider += "\n"

        returnString += divider
        for y in range(0, self.boardSize):
            returnString += str(y)
            for x in range(0, self.boardSize):
                if self.board[x][y].mine and self.board[x][y].selected:
                    returnString += " |" + str(self.board[x][y].value)
                elif self.board[x][y].selected:
                    returnString += " | " + str(self.board[x][y].value)
                else:
                    returnString += " |  "
            returnString += " |"
            returnString += divider
        return returnString

    def addMine(self, x, y):
        self.board[x][y].value = -1
        self.board[x][y].mine = True
        for i in range(x-1, x+2):
            if i >= 0 and i < self.boardSize:
                if y-1 >= 0 and not self.board[i][y-1].mine:
                    self.board[i][y-1].value += 1
                if y+1 < self.boardSize and not self.board[i][y+1].mine:
                    self.board[i][y+1].value += 1
        if x-1 >= 0 and not self.board[x-1][y].mine:
            self.board[x-1][y].value += 1
        if x+1 < self.boardSize and not self.board[x+1][y].mine:
            self.board[x+1][y].value += 1

    def makeMove(self, x, y):
        self.board[x][y].selected = True
        self.selectableSpots -= 1
        if self.board[x][y].value == -1:
            return False
        if self.board[x][y].value == 0:
            for i in range(x-1, x+2):
                if i >= 0 and i < self.boardSize:
                    if y-1 >= 0 and not self.board[i][y-1].selected:
                        self.makeMove(i, y-1)
                    if y+1 < self.boardSize and not self.board[i][y+1].selected:
                        self.makeMove(i, y+1)
            if x-1 >= 0 and not self.board[x-1][y].selected:
                self.makeMove(x-1, y)
            if x+1 < self.boardSize and not self.board[x+1][y].selected:
                self.makeMove(x+1, y)
            return True
        else:
            return True

    def hitMine(self, x, y):
        return self.board[x][y].value == -1

    def isWinner(self):
        return self.selectableSpots == 0


#play game
def playGame():
    boardSize = int(input("Choose the Width of the board: "))
    numMines = int(input("Choose the number of mines: "))
    gameOver = False
    winner = False
    Board = boardClass(boardSize, numMines)
    while not gameOver:
        print(Board) 
        print("Make your move:")
        x = int(input("x: "))
        y = int(input("y: "))
        Board.makeMove(x, y)
        gameOver = Board.hitMine(x, y)
        if Board.isWinner() and gameOver == False:
            gameOver = True
            winner = True

    print(Board)
    if winner:
        print("Congratulations, You Win!")
    else:
        print("You hit a mine, Game Over!")

playGame()
plant_bombs()
print_board()