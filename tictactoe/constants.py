import pygame

WIDTH = HEIGHT = 600 # dimensions of game window
ROWS = COLS = 3 # number of grid rows and columns
SQUARE_SIZE = HEIGHT // ROWS # the pixel dimensions of each square

# colour RGB values stored as a list
BLACK = [0,0,0]
WHITE = [255,255,255]

# load and scale the cross image from assets
X_ICON = pygame.transform.scale(pygame.image.load("files/assets/x-icon.jpeg"), (SQUARE_SIZE-30, SQUARE_SIZE-30))
