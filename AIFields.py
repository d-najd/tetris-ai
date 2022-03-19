import math


def calHoles(board, shape, startX, startY):
    """
    calculates the amount of holes that will be generated if a piece is placed
    :return: the amount of holes
    """
    startY -= 1
    score = 0  # the smaller the worse
    for x in range(startX, len(shape[0]) + startX):
        x = x
        toIgnore = ignoreSpots(shape,
                               x - startX)  # TODO optimize this in future so we don't calculate this multiple times
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


def calBumpiness(board):
    score = 0
    lastHitPos = -1
    for x in range(0, len(board[0])):
        for y in range(0, len(board)):
            if board[y][x] != 0:
                if lastHitPos != -1:
                    score -= math.fabs(lastHitPos - y)
                    lastHitPos = y
                    break
                else:
                    lastHitPos = y
                    break
    return score


def calBigHole(board):
    # TODO check if this works correctly
    score = 0
    lastHitPos = -1
    for x in range(0, len(board[0])):
        for y in range(0, len(board)):
            if board[y][x] != 0:
                if lastHitPos != -1:
                    if math.fabs(lastHitPos - y) > 3:
                        score -= 1
                    lastHitPos = y
                    break
                else:
                    lastHitPos = y
                    break
    return score


def calHolesAboveEPiece(board, pieceAboveMultiplier):
    # TODO test if this works
    score = 0
    ignorePieceAboveMultiplier = False
    if pieceAboveMultiplier == 0:
        ignorePieceAboveMultiplier = True
    for x in range(0, len(board[0])):
        piecesAbove = 0
        for y in range(0, len(board) - 1):
            if piecesAbove != 0:
                if board[y][x] == 0:
                    if not ignorePieceAboveMultiplier:
                        score -= piecesAbove * pieceAboveMultiplier
                    else:
                        score -= 1
                else:
                    piecesAbove += 1
            elif board[y][x] != 0:
                piecesAbove += 1
    return score


def ignoreSpots(shape, x):
    toIgnore = 0
    for i in range(0, len(shape)):
        if shape[i][x] != 0:
            toIgnore -= 1
    return toIgnore
