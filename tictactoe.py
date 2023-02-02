"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCounter = 0
    oCounter = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] == X:
                xCounter += 1
            if board[row][col] == O:
                oCounter += 1

    if xCounter > oCounter:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    enabledActions = set();

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                enabledActions.add((row, col))

    return enabledActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not valid move")

    copiedBoard = copy.deepcopy(board)
    row, col = action
    copiedBoard[row][col] = player(board)
    return copiedBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
 
    for i in range(3):        
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
        
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def maxValue(board):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        result_value = minValue(result(board, action))
        if result_value == 1:
            return 1
        value = max(value, result_value)
    return value


def minValue(board):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        result_value = maxValue(result(board, action))
        if result_value == -1:
            return -1
        value = min(value, result_value)
    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        value = -math.inf
        optimal_action = None
        for action in actions(board):
            result_value = minValue(result(board, action))
            if result_value == 1:
                return action
            if result_value > value:
                value = result_value
                optimal_action = action
        return optimal_action
    else:
        value = math.inf
        optimal_action = None
        for action in actions(board):
            result_value = maxValue(result(board, action))
            if result_value == -1:
                return action
            if result_value < value:
                value = result_value
                optimal_action = action
        return optimal_action
    
    
    
