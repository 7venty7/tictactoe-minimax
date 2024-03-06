import pygame
from .constants import HEIGHT, WIDTH, ROWS, COLS, SQUARE_SIZE, BLACK, WHITE, X_ICON

PADDING = 10

class Board:
    def __init__(self):
        self.board = []
        self.noughts = self.crosses = 0
        self.create_board()

    # create the initial 3x3 matrix and initialise all grid places to be 0 i.e. no nought/cross
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            
            for col in range(COLS):
                self.board[row].append(0)

    # draw in the base board
    def draw_squares(self, win):
        win.fill(BLACK)

        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, WHITE, (col*SQUARE_SIZE + PADDING, row*SQUARE_SIZE + PADDING, SQUARE_SIZE - 2*PADDING, SQUARE_SIZE - 2*PADDING))
    
    # draw in all of the placed noughts/crosses in their respective grid places
    def draw_board(self, win):
        self.draw_squares(win)

        for row in range(ROWS):
            for col in range(COLS):
                # calculate the centre of the square on the grid
                centre_x = SQUARE_SIZE * col + (SQUARE_SIZE // 2)
                centre_y = SQUARE_SIZE * row + (SQUARE_SIZE // 2)

                # draw crosses from clipart image in assets directory
                if self.board[row][col] == "X":
                    win.blit(X_ICON, (centre_x - X_ICON.get_width()//2, centre_y - X_ICON.get_height()//2))
                
                # draw noughts by drawing 2 overlapping circles
                elif self.board[row][col] == "O":
                    radius = int(0.8*((SQUARE_SIZE-2*PADDING) // 2))
                    
                    pygame.draw.circle(win, BLACK, (centre_x, centre_y), radius)
                    pygame.draw.circle(win, WHITE, (centre_x, centre_y), 0.5*radius)



    