"""
Travese matrix in a spiral fashion
"""
import pdb


def convert_spiral(matrix):
    """
    @param matrix: List of list of ints.
    """
    spiral = []
    top = 0
    bottom = len(matrix)
    left = 0
    right = len(matrix[0])
    direction = 'forward'
    while (left < right) and (top < bottom):

        # go forward
        if direction == 'forward':
            for i in matrix[top][left:right]:
                spiral.append(i)
            top += 1  # move top border down 1 row
            direction = 'down'

        # go down
        elif direction == 'down':
            for i in range(top, bottom):
                spiral.append(matrix[i][right-1])
            right -= 1
            direction = 'backward'

        # go backwards
        elif direction == 'backward':
            for i in range(right-1, left-1, -1):
                spiral.append(matrix[bottom-1][i])
            bottom -= 1
            direction = 'up'

        # go up
        elif direction == 'up':
            for i in range(bottom-1, top-1, -1):
                spiral.append(matrix[i][left])
            left += 1
            direction = 'forward'

    return spiral


# test cases
input1 = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]

input2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]]

input3 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]]


input3 = [[]]

assert(convert_spiral(input1) == [1,2,3,6,9,8,7,4,5])
assert(convert_spiral(input2) == [1,2,3,4,8,12,11,10,9,5,6,7])
assert(convert_spiral(input3) == [])
