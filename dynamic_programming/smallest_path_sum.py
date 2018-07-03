"""
Given a m x n self.grid filled with non-negative numbers, find a path from top left to bottom right
which minimizes the sum of all numbers along its path.

Assume 0 <= self.grid[i][j] < 10

python -mtimeit -s'from dynamic_programming.smallest_path_sum import MinPathSum' 'MinPathSum(70, 70).recursive()'
python -mtimeit -s'from dynamic_programming.smallest_path_sum import MinPathSum' 'MinPathSum(70, 70).dp()'
"""
import numpy as np
import random
__author__ = 'Gary Tang'


class MinPathSum:

    def __init__(self, m=10, n=10):
        # init grid with user input
        self.grid = [[random.randint(0, 9) for i in range(m)] for j in range(n)]

    def recursive(self):
        """
        recursive solution
        """
        memo = []
        def traverse(row, col, total):
            """Helper function that essentially keeps moving down and right until
            we reach the end."""

            total += self.grid[row][col]
            # base case. Reach bottom right-most corner. Save value
            if (row == len(self.grid)-1) and (col == len(self.grid[0])-1):
                memo.append(total)
                return

            if row < len(self.grid)-1:
                # move down
                traverse(row+1, col, total)
            if col < len(self.grid[row])-1:
                # move right
                traverse(row, col+1, total)
        traverse(0, 0, 0)
        return min(memo)


    def dp(self):
        """
        dynamic programming solution. O(n*m)
        """
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                # visit cells from left to right, top to bottom
                # need to check boundary
                if row > 0:
                    if col > 0:
                        self.grid[row][col] += min(self.grid[row-1][col], self.grid[row][col-1])
                    else:
                        # on leftmost edge
                        self.grid[row][col] += self.grid[row-1][col]
                else:
                    if col > 0:
                        self.grid[row][col] += self.grid[row][col-1]
        return self.grid[-1][-1]


