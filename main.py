import pygame
import sys
from tictactoe.constants import HEIGHT, WIDTH, SQUARE_SIZE
from tictactoe.game import Game
from minimax.algorithmv2 import findBestMove

# Display FPS
FPS = 60

# Display window with dimensions 600x600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Function to get a square on the grid from mouse position
def get_square(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    
    # main loop
    while run:
        clock.tick(FPS)

        # if the game has ended close the game
        if game.check_win() or game.check_draw():
            break
        
        # if it is the ai's turn, compute the best possible move and play it
        if game.turn == ai_player:
            aimove = findBestMove(game.get_board(), game)
            game.place(aimove[0], aimove[1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # Execute place function at the grid coordinate returned from get_square when a mouse click is detected
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_square(pos)
                game.place(row,col)

        # update the game state
        game.update()
    
    pygame.quit()


# get user input for which piece the ai should play as
if len(sys.argv) != 2 or sys.argv[1] not in ["X", "O"]:
    print("Usage: python main.py [ai player (X,O)]")
else:
    ai_player = sys.argv[1]
    main()
        
