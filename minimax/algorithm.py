import pygame
from copy import deepcopy 

COLS = ROWS = 3

def minimax(position, depth, max_player, game):
    if depth == 0 or game.check_win() or game.turn_count >= 9:
        return game.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None

        for row in range(ROWS):
            for col in range(COLS):
                if position[row][col] == 0:
                    newpos = deepcopy(position)
                    position[row][col] = 'X'
                    
                    evaluation = minimax(position, depth-1, False, game)[0]
                    maxEval = max(evaluation, maxEval)

                    position[row][col] = 0

                    if maxEval == evaluation:
                        best_move = [row,col]
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None

        for row in range(ROWS):
            for col in range(COLS):
                if position[row][col] == 0:
                    newpos = deepcopy(position)
                    position[row][col] = game.turn

                    evaluation = minimax(position, depth-1, True, game)[0]
                    minEval = min(evaluation, minEval)

                    position[row][col] = 0

                    if minEval == evaluation:
                        best_move = [row,col]
        return minEval, best_move