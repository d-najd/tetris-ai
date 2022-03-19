import math
from copy import deepcopy

import AIFields
import game

cols = game.cols
rows = game.rows

# region scoreMultipliers
holesMultiplier = 2
bumpinessMultiplier = 1.5
heightMultiplier = 1.2
bigHoleMultiplier = 5
holesAboveEmptyPieceMultiplier = 3
# multiplier for the number of spots above the empty piece, if left to 0 will be ignored and just add 1 to the score
subHolesAboveEmptyPieceM = 0


# endregion

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


def calPosScore(board, shape, startX, startY):
    """
    calculates the score on a given position
    :param startY:
    :param startX:
    :param board: board containing the piece
    :param shape: the piece
    :return: the score given to a spot, 0 is the best possible score
    """

    score = 0
    score += AIFields.calHoles(board, shape, startX, startY) * holesMultiplier
    score += AIFields.calBumpiness(board) * bumpinessMultiplier
    score += AIFields.calBigHole(board) * bigHoleMultiplier
    score += AIFields.calHolesAboveEPiece(board, subHolesAboveEmptyPieceM)
    score += (math.fabs(startY - len(board)) * heightMultiplier) * -1
    return score


def ignoreSpots(shape, x):
    toIgnore = 0
    for i in range(0, len(shape)):
        if shape[i][x] != 0:
            toIgnore += 1
    return toIgnore
