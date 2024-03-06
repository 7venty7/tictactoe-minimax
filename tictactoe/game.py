import pygame
from .constants import ROWS, COLS
from .board import Board

# stores all game mechanics
class Game:
    def __init__(self, win):
        self.board = Board()
        self.turn = "X"
        self.win = win
        self.last_move = None
        self.winner = None
    
    # update function redraws the board with new placed pieces and checks if there has been a winner
    def update(self):
        if self.check_win() != None:
            self.winner = self.check_win()
            print("Winner: ", self.winner)
        elif self.check_draw():
            print("Draw")

        self.board.draw_board(self.win)
        pygame.display.update()

    # function that checks if there is a nought/cross at the given grid matrix position and if not places a nought/cross there depending on the turn
    # sets the grid coordinate of the placement and the piece that was placed (X or O) to the list variable last_move so that the move can be checked for deciding a win or not
    def place(self, row, col):
        if self.board.board[row][col] == 0:
            self.board.board[row][col] = self.turn
            self.last_move = [row, col, self.turn]

            self.change_turn()
            return True
        else:
            return False
        
    # cycle the player turns
    def change_turn(self):
        if self.turn == "X":
            self.turn = "O"
        else:
            self.turn = "X"

    # checks if there is a winner on the board
    def check_win(self):
        if self.check_diag() or self.check_horizontal() or self.check_vertical():
            return self.last_move[2]
        else:
            return None
    
    # checks the 2 diagonals of the board if the last move was placing a nought/cross at a grid position that could make a diagonal
    def check_diag(self):
        if not self.last_move:
            return False
        
        if (self.last_move[1] == 1 and self.last_move[0] in [0,2]) or (self.last_move[0] == 1 and self.last_move[1] in [0,2]):
            return False
        
        count = 0
        for i in range(ROWS):
            if self.board.board[i][i] != self.last_move[2]:
                break
            else:
                count += 1

        if count >= 3:
            return True

        count = 0
        for i in range(ROWS):
            if self.board.board[ROWS - i - 1][i] != self.last_move[2]:
                break
            else:
                count += 1
        
        if count >= 3:
            return True
        else:
            return False

    # check the horizontal row of the piece that was last placed to check for a win
    def check_horizontal(self):
        if not self.last_move:
            return False
        
        for col in range(COLS):
            if self.board.board[self.last_move[0]][col] != self.last_move[2]:
                return False
            
        return True
        
    # check the vertical column of the piece that was last placed to check for a win
    def check_vertical(self):
        if not self.last_move:
            return False
        
        for row in range(ROWS):
            if self.board.board[row][self.last_move[1]] != self.last_move[2]:
                return False
            
        return True
    
    # evaluate the score of the current position for the minimax algorithm, return 10 if X wins, -10 if O wins or 0 if no win
    def evaluate(self):
        if self.check_win() == "X":
            return 10
        elif self.check_win() == "O":
            return -10
        else:
            return 0
        
    # check if there are any available moves left on the board
    def check_draw(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.board[row][col] == 0:
                    return False
        
        return True
    
    
    def get_board(self):
        return self.board.board
        