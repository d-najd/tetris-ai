import time

import game
from copy import deepcopy

cols = game.cols
rows = game.rows


# returns the list of actions needed to be performed to reach the best possible position
def returnBestPos(board_, shape_):
    bestScore = -10000000000
    bestScoreX = -1
    bestScoreRotation = -1
    shape = shape_[:]
    # iterates through all possible places where a piece can be placed
    for rotation in range(0, 4):  # all rotations where the piece can be placed
        if rotation != 0:
            shape = game.rotate_clockwise(shape)
        for x in range(0, cols + 1 - len(shape[0])):  # all possible x positions for given rotation
            board = deepcopy(board_)  # find a way to make immutable 2d lists
            y = 0
            while not game.check_collision(board, shape, (x, y)):
                y += 1
            endPos = game.join_matrixes(board, shape, (x, y))
            curScore = calPosScore(endPos, shape, x, y)
            if curScore > bestScore:
                bestScore = curScore
                bestScoreX = x
                bestScoreRotation = rotation
    print(bestScoreX, bestScoreRotation)
    return bestScoreX, bestScoreRotation


# board will be the board with the piece in it
# shape is the piece
# startX is the position where the piece begins, we should be able to use this to calculate the range it occupies
# starY the height that he piece is currently at

def calPosScore(board, shape, startX, startY):
    # calculates the score of a given position
    startY -= 1
    score = 0 #the smaller the worse
    for x in range(startX, len(shape[0]) + startX):
        x = x
        toIgnore = ignoreSpots(shape, x - startX)  # TODO optimize this in future so we don't calculate this multiple times
        hitpart = False
        for y in range(startY, len(board) - 1):
            if board[y][x] != 0:
                if toIgnore == 0:
                    break
                hitpart = True
                toIgnore -= 1
            elif board[y][x] == 0 and hitpart:
                score -= 1
    return score


def ignoreSpots(shape, x):
    toIgnore = 0
    for i in range(0, len(shape)):
        if shape[i][x] != 0:
            toIgnore += 1
    return toIgnore
