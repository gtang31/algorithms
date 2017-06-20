"""
Given a matrix M with size NxN, rotate it by 90 degrees in-place.
"""
import numpy as np
__author__ = "Gary Tang"


class rotateMatrixSolution(object):

    def __init__(self, M, rotate_by=90):
        self._rotate_by = rotate_by
        self._M = M
        self._N = len(M)

    def rotate_inplace(self):
        """
        Rotate the values in M in-place starting from the corners in the outer
        'layer' and moving inwards toward the center. The trick is knowing how
        to swap the values in M. Run time is also O(n^2) but constant space.
        """
        layer = 0
        for row in range(-(-self._N//2)):
            for col in range(layer, self._N-layer-1):
                # use in-place swapping, starting with corners and then rotate
                # in clock-wise direction until we get to the center
                self._M[row][col], self._M[col][self._N-1-row], self._M[self._N-1-layer][self._N-1-col], self._M[self._N-1-col][row] = \
                    self._M[self._N-1-col][row], self._M[row][col], self._M[col][self._N-1-row], self._M[self._N-1-layer][self._N-1-col]
            layer += 1
        return np.array(self._M)

    def rotate(self):
        """
        Create a new matrix and populate it with values from M starting from
        bottom left corner. Iterate from bottom to top, left to right. This
        solution will require O(n^2) run-time and additional space.
        """
        new_M = []
        for col in range(self._N):
            temp = []  # row in new matrix
            for row in range(self._N-1, -1, -1):
                # starting from bottom row of M
                temp.append(self._M[row][col])
            new_M.append(temp)
        return new_M


# Test cases
assert np.array_equal(rotateMatrixSolution([[1, 2], [3, 4]]).rotate(), np.rot90([[1, 2], [3, 4]], -1))
assert np.array_equal(rotateMatrixSolution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).rotate(), np.rot90([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1))
assert np.array_equal(rotateMatrixSolution([[1]]).rotate(), np.rot90([[1]], -1))
assert np.array_equal(rotateMatrixSolution([[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12], [13, 14, 15, 16]]).rotate(), np.rot90([[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12], [13, 14, 15, 16]], -1))

assert np.array_equal(rotateMatrixSolution([[1, 2], [3, 4]]).rotate_inplace(), np.rot90([[1, 2], [3, 4]], -1))
assert np.array_equal(rotateMatrixSolution([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).rotate_inplace(), np.rot90([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1))
assert np.array_equal(rotateMatrixSolution([[1]]).rotate_inplace(), np.rot90([[1]], -1))
assert np.array_equal(rotateMatrixSolution([[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12], [13, 14, 15, 16]]).rotate_inplace(), np.rot90([[1, 2, 3, 10], [4, 5, 6, 11], [7, 8, 9, 12], [13, 14, 15, 16]], -1))
assert np.array_equal(rotateMatrixSolution([[1, 2, 3, 10, 17], [4, 5, 6, 11, 18], [7, 8, 9, 12, 19], [13, 14, 15, 16, 20], [21, 22, 23, 24, 25]]).rotate_inplace(), np.rot90([[1, 2, 3, 10, 17], [4, 5, 6, 11, 18], [7, 8, 9, 12, 19], [13, 14, 15, 16, 20], [21, 22, 23, 24, 25]], -1))
