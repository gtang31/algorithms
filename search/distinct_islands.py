"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""
import numpy as np
import pdb


class Solution:
    def count_islands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set() # Track cells we have visited. Use set for O(1) look time
        self.num_islands = 0

        def dfs(cell):
            """depth-first search helper function"""
            r, c = cell
            if (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and (cell not in visited) and (grid[r][c] != 0):

                visited.add((r, c))  # save cell
                grid[r][c] = self.num_islands
                # update current island size
                dfs((r, c+1))
                dfs((r+1, c))
                dfs((r-1, c))
                dfs((r, c-1))

            else:
                # out of bounds or visited
                return

        # traverse the grid and explore the size of islands we visit
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == 0) or ((row, col) in visited):
                    continue
                else:
                    self.num_islands += 1
                    dfs((row, col))

        print(np.array(grid))
        return self.num_islands


g = [['X', 'X', 0, 0, 0]
    ,['X', 'X', 0, 0, 0]
    ,['X', 0, 0, 'X', 'X']
    ,['X', 0, 'X', 0, 0]]
Solution().count_islands(g)

g = [["X", "X", 0, 0, 0]
    ,["X", "X", 0, 0, 0]
    ,[0, 0, "X", 0, 0]
    ,[0, 0, 0, "X", "X"]]
Solution().count_islands(g)
