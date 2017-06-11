"""
Imagine a robot sitting on the upper left corner of grid with r rows and c
columns. The robot can only move in two directions, right and down, but certain
cells are "off limits" such that the robot cannot step on them. Design an
algorithm that calculates the number of different paths the robot can take to
reach the end. To compare the time difference:

python -mtimeit -s'from dynamic_programming.possible_paths import CountPaths' "grid = [['s', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'X', 'o', 'o', 'o', 'X', 'o'],
        ['o', 'o', 'o', 'o', 'o', 'X', 'o', 'o', 'o'],
        ['X', 'o', 'o', 'X', 'o', 'o', 'X', 'o', 'o'],
        ['o', 'o', 'o', 'X', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'X', 'X', 'o', 'X', 'o'],
        ['o', 'X', 'o', 'o', 'o', 'o', 'X', 'o', 'o'],
        ['o', 'X', 'o', 'o', 'o', 'o', 'X', 'o', 'o'],
        ['o', 'X', 'o', 'o', 'o', 'o', 'X', 'o', 'o'],
        ['o', 'X', 'o', 'o', 'o', 'o', 'X', 'o', 'o'],
        ['o', 'X', 'o', 'o', 'o', 'o', 'X', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 't']]" 'CountPaths(grid).recursion()'
python -mtimeit -s'from dynamic_programming.possible_paths import CountPaths' "grid = [['s', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'X', 'o', 'o', 'o', 'X', 'o'],
        ['o', 'o', 'o', 'o', 'o', 'X', 'o', 'o', 'o'],
        ['X', 'o', 'o', 'X', 'o', 'o', 'X', 'o', 'o'],
        ['o', 'o', 'o', 'X', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'X', 'X', 'o', 'X', 'o'],
        ['o', 'X', 'o', 'o', 'o', 'o', 'X', 'o', 'o'],
        ['o', 'X', 'o', 'o', 'o', 'o', 'X', 'o', 'o'],
        ['o', 'X', 'o', 'o', 'o', 'o', 'X', 'o', 'o'],
        ['o', 'X', 'o', 'o', 'o', 'o', 'X', 'o', 'o'],
        ['o', 'X', 'o', 'o', 'o', 'o', 'X', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 't']]" 'CountPaths(grid).top_down()'
"""
import numpy as np
from random import randint
__author__ = 'Gary Tang'


class CountPaths(object):

    def __init__(self, grid):
        self.grid = grid
        self.r_dim, self.c_dim = len(grid)-1, len(grid[0])-1

    def recursion(self, r=0, c=0):
        """
        Recursion solution takes O(2^(r+c)) due to multiple cells being visited
        twice.
        """
        if self.grid[r][c] == 'X':
            # dead end
            return 0
        elif self.grid[r][c] == 't':
            # target endpoint found
            return 1
        elif (r == self.r_dim) and (c < self.c_dim):
            # check bottom boundary
            self.grid[r][c] = self.recursion(r, c+1)
            return self.grid[r][c]
        elif (c == self.c_dim) and (r < self.r_dim):
            # check right boundary
            self.grid[r][c] = self.recursion(r+1, c)
            return self.grid[r][c]
        else:
            self.grid[r][c] = self.recursion(r+1, c) + self.recursion(r, c+1)
            return self.grid[r][c]

    def top_down(self):
        """
        top-down approach that saves the steps for each cells. Reduces time
        complexity to O(rc)
        """
        memo = {}

        def recurse(r=0, c=0):
            if (r, c) in memo:
                return memo[(r, c)]
            elif self.grid[r][c] == 't':
                memo[(r, c)] = 1
            elif self.grid[r][c] == 'X':
                memo[(r, c)] = 0
            elif (r == self.r_dim) and (c < self.c_dim):
                memo[(r, c)] = recurse(r, c+1)
                self.grid[r][c] = memo[(r, c)]
            elif (c == self.c_dim) and (r < self.r_dim):
                memo[(r, c)] = recurse(r+1, c)
                self.grid[r][c] = memo[(r, c)]
            else:
                memo[(r, c)] = recurse(r+1, c) + recurse(r, c+1)
                self.grid[r][c] = memo[(r, c)]
            return memo[(r, c)]
        return recurse()


if __name__ == "__main__":
    # construct a random grid size
    rows = randint(2, 20)
    cols = randint(2, 12)
    grid = []
    for i in xrange(rows):
        grid.append(['o']*cols)

    # populate grid with start/target/obstacles
    grid[0][0], grid[rows-1][cols-1] = 's', 't'
    for i in xrange(randint(0, (rows*cols-2)/2)):
        r, c = randint(0, rows-1), randint(0, cols-1)
        if (r == 0 and c == 0) or (r == rows-1 and c == cols-1):
            continue
        grid[r][c] = 'X'

    h = CountPaths(grid)
    h.recursion()
    g = CountPaths(grid)
    g.top_down()
    assert(np.array_equal(np.array(h.grid), np.array(g.grid)) is True)
    print(np.array(g.grid))
