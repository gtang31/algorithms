"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
Ex:
[[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
 [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
Biggest island is of size 6
"""
import numpy as np
import random
__author__ = 'Gary Tang'


class Solution:
    def __init__(self):
        self.largest_size = 0

    def find_largest_island(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set() # Track cells we have visited. Use set for O(1) look time

        def dfs(cell):
            """depth-first search helper function"""
            r, c = cell
            if (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and (cell not in visited) and (grid[r][c] != 0):

                visited.add((r, c))  # save cell

                # update current island size
                grid[r][c] += sum([dfs((r, c+1)) , dfs((r+1, c)) , dfs((r-1, c)) , dfs((r, c-1))])
                self.largest_size = max(self.largest_size, grid[r][c])
                return grid[r][c]

            else:
                # out of bounds or visited
                return 0

        # traverse the grid and explore the size of islands we visit
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == 0) or ((row, col) in visited):
                    continue
                else:
                    dfs((row, col))

        print(np.array(grid)) # check results
        return self.largest_size

g = [[1, 1, 1, 0],
     [1, 1, 0, 0]]
assert(Solution().find_largest_island(g) == 5)
print('*'*10)

g = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
assert(Solution().find_largest_island(g) == 6)
print('*'*10)

g = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
assert(Solution().find_largest_island(g) == 25)


