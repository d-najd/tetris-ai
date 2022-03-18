import game
from copy import deepcopy

cols = game.cols
rows = game.rows


# returns the list of actions needed to be performed to reach the best possible position
def returnBestPos(board_, shape_):
    print("test")
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
            calPosScore(endPos, shape, x, y)


"""
I should be able to use the board and xrange to calculate how much empty spaces are in the given range, we can do this 
by lighting a ray from top like so

0 0 0 0 0
0 1 1 0 0
0 0 1 1 0 

to

9 9 9 9 9
9 1 1 9 9
9 0 1 1 9

and calculate the amount of 0's in the grid

    ###########
    ###NOTE####
    ###########

we should ignore the piece 1's and if we hit a 1 which isn't from our piece then we should move to the next position in
the range
"""


# board will be the board with the piece in it
# shape is the piece
# startX is the position where the piece begins, we should be able to use this to calculate the range it occupies
# starY the height that he piece is currently at

def calPosScore(board, shape, startX, startY):
    # calculates the score of a given position
    startY -= 1
    for x in range(startX, len(shape[0]) + startX):
        # calculate how many spots to ignore based on the shape
        for y in range(startY, len(board) - 1):
            print("x " + str(x) + " y " + str(y))
