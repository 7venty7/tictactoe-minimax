COLS = ROWS = 3

# fixed version of minimax algorithm
def minimax(board, depth, max_player, game):
    score = game.evaluate()

    if score == 10:
        # subtract depth from the score of 10 when crosses wins, as rate board states where winning takes longer, lower
        return score - depth
    elif score == -10:
        # add depth to the score of -10 when noughts wins, as rate board states where winning takes longer, lower
        return score + depth
    elif game.check_draw():
        # if there is a draw, return 0
        return 0
    
    # if it is the maximiser's turn (crosses)
    if max_player:
        # set the best score the maximiser has seen so far to -1000 i.e. any move is better
        maxEval = -1000

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 0:
                    # if there is an available move, play it
                    board[row][col] = "X"
                    game.last_move = [row, col, "X"]

                    # recursively run the minimax function for the minimiser pieces such as to evaluate further board states from this move
                    # determine the minimum of the current lowest board score or the scores of future board states
                    maxEval = max(maxEval, minimax(board, depth+1, False, game))

                    # undo the move
                    board[row][col] = 0

        return maxEval
    else:
        # set the best score the minimiser has seen so far to 1000 i.e. any move is better
        minEval = 1000

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 0:
                    # if there is an available move, play it
                    board[row][col] = "O"
                    game.last_move = [row, col, "O"]

                    # recursively run the minimax function for the maximiser pieces such as to evaluate further board states from this move
                    # determine the minimum of the current lowest board score or the scores of future board states
                    minEval = min(minEval, minimax(board, depth+1, True, game))

                    # undo the move
                    board[row][col] = 0

        return minEval 
    
def findBestMove(board, game):
    # initialise the best_move variable to store the best possible move, which will be played by the ai
    best_move = None

    if game.turn == "X":
        maxEval = -1000

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 0:
                    board[row][col] = "X"
                    game.last_move = [row, col, "X"]
                    evaluation = minimax(board, 0,False, game)
                    board[row][col] = 0

                    # if the evaluation of this move is the best so far, assign the move to the best_move variable
                    if evaluation >  maxEval:
                        best_move = [row, col]
                        maxEval = evaluation
        
        return best_move
    else:
        minEval = 1000

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 0:
                    board[row][col] = "O"
                    game.last_move = [row, col, "O"]
                    evaluation = minimax(board, 0,True, game)
                    board[row][col] = 0

                    # if the evaluation of this move is the best so far, assign the move to the best_move variable
                    if evaluation <  minEval:
                        best_move = [row, col]
                        minEval = evaluation
        
        return best_move
