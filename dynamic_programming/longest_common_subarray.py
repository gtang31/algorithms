"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
This problem is also very similar to longest common substring problem
"""
import numpy as np
__author__ = 'Gary Tang'


class LongestSubarray(object):
    def findLength(self, A, B):
        """
        Create a 2D Array[i][j] where i and j are lengths or A and B, respectively. 
        Use the Array to keep track of matching elements from both arrays.
        Increment Array[i][j] if A[i-1][j-1] >= 1
        param A: list. A[i] is an int
        param B: list. B[i] is an int
        rtype longest: int
        """
        memo = np.array([[0 for col in range(len(A)+1)] for row in range(len(B)+1)])  # add extra row/col for padding

        # double for-loop to go through each array and compare each individual char
        # O(a*b) time-complexity
        for row, i in enumerate(B):
            for col, j in enumerate(A):
                if j == i:
                    # for the current cell in memo, set it equal
                    # to previous diagonal cell + 1.
                    # Hence the padding we added to memo during the init to
                    # avoid boundary checking
                    memo[row+1][col+1] = memo[row][col]+1

        longest = 0
        for row in range(len(memo)):
            for col in range(len(memo[row])):
                longest = max(longest, memo[row][col])

        # re-write 0-th row and column in 2D array for easy validation when printing
        memo[0] = [0]+A
        for row in range(1, len(memo)):
            memo[row][0] = B[row-1]

        print(memo)
        return longest





A = [1,2,3,2,1]
B = [3,2,1,4,7]
assert(LongestSubarray().findLength(A, B) == 3)

A = [1,3,5,6,2,4,5,6,7,8,9,4,5]
B = [2,3,4,5,7,8,2,33,4,5,6,7,8,9,1,2,4,5,7,8]
assert(LongestSubarray().findLength(A, B) == 6)
