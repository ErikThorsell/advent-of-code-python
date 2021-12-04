import numpy as np


def play_one_number(boards, matches, number):
    for bx, board in enumerate(boards):
        match = np.where(board == number)
        if match:
            matches[bx][match] = 1
    return matches


def has_bingo(match):
    for r in range(match.shape[0]):
        if np.all(match[r] == 1):
            return True
    for c in range(match.T.shape[0]):
        if np.all(match.T[c] == 1):
            return True
    return False


def sum_unmatched(board, match):
    unmarked = np.argwhere(match == 0)
    s = 0
    for um in unmarked:
        s += board[um[0], um[1]]
    return int(s)
