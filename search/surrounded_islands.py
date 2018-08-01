"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""
import numpy as np
__author__ = "Gary Tang"


class Solution:
    def is_surrounded(self, grid):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        visited = set() # Track cells we have visited. Use set for O(1) look time

        def dfs(cell):
            """depth-first search helper function"""
            r, c = cell
            if ((r == len(grid)-1) or (c == len(grid[0])-1) or (c == 0) or (r == 0)) and (grid[r][c] == 'O'):
                # Island borders edge of grid
                return False
            elif (grid[r][c] == 'X') or (cell in visited):
                return True
            else:
                visited.add(cell)

                # visit neighbor cells and check whether it is surrounded
                if dfs((r+1, c)) and dfs((r, c+1)) and dfs((r-1, c)) and dfs((r, c-1)):
                    grid[r][c] = 'X'
                    return True
                else:
                    return False

        # traverse the grid and explore the size of islands we visit
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == 'X') or ((row, col) in visited):
                    continue
                else:
                    dfs((row, col))

        print(np.array(grid))


g = [['X', 'X', 'X', 'X']
    ,['X', 'O', 'O', 'X']
    ,['X', 'X', 'O', 'X']
    ,['X', 'O', 'X', 'X']]
Solution().is_surrounded(g)

g = [['O', 'X', 'X', 'O']
    ,['X', 'O', 'O', 'X']
    ,['X', 'X', 'O', 'X']
    ,['O', 'X', 'O', 'O']]
Solution().is_surrounded(g)

g = [['O', 'O', 'X', 'O']
    ,['X', 'X', 'X', 'X']
    ,['X', 'X', 'O', 'X']
    ,['O', 'X', 'X', 'O']]
Solution().is_surrounded(g)

g = [['O', 'O', 'X', 'O']
    ,['O', 'X', 'X', 'X']
    ,['O', 'O', 'O', 'X']
    ,['X', 'X', 'X', 'O']]
Solution().is_surrounded(g)
