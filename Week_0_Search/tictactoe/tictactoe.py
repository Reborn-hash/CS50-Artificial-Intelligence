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
    values = [i for n in board for i in n]
    xs = values.count("X")
    os = values.count("O")

    if xs == os:
        return "X"
    else:
        return "O"

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] is None:
                moves.add((i,j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    a = copy.deepcopy(board)
    """if board[action[0]-1][action[1]-1] is not None:
        print("That move is already taken")
        return board"""
    a[action[0]][action[1]] = player(board)

    return a


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    a = (board[0][0],board[1][1],board[2][2])
    b = (board[0][2],board[1][1],board[2][0])
    c = (board[0][0],board[1][0],board[2][0])
    d = (board[0][1],board[1][1],board[2][1])
    e = (board[0][2],board[1][2],board[2][2])
    f = (board[0][0],board[0][1],board[0][2])
    g = (board[1][0],board[1][1],board[1][2])
    h = (board[2][0],board[2][1],board[2][2])
    for n in [a,b,c,d,e,f,g,h]:
        if ("X","X","X") == n:
            return "X"
        elif ("O","O","O") == n:
            return "O"
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    return winner(board) is not None or None not in [i for n in board for i in n]

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if player(board) == "X":
        max_value(board)
        return action_
    else:
        min_value(board)
        return action_

action_ = ()

def max_value(board):
    v = -100
    if terminal(board):
        return utility(board)
    maxa = [v,None]
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
        if v > maxa[0]:
            maxa[1] = action
            maxa[0] = v
    global action_
    if maxa[1] is not None:
        action_ = maxa[1]
    return v


def min_value(board):
    v = 100
    if terminal(board):
        return utility(board)
    mina = [v, None]
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
        if v < mina[0]:
            mina[1] = action
            mina[0] = v
    global action_
    if mina[1] is not None:
        action_ = mina[1]
    return v


