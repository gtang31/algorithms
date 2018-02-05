'''
Search for a word in a 2D grid. A word is "found" as long as each consecutive
letter can be found in an adjacent cell. A cell is considered to be adjacent if
the cell is directly top, bottom, left, or right to the current cell in the grid.
'''
__author__ = 'Gary Tang'


class FindWord2D(object):

    def __init__(self, grid, word):
        self.word = word
        self.grid = grid
        self.size = [len(grid)-1, len(grid[0])-1]

    def search_word(self, row, col, pos, my_word):
        """
        Use DFS search to determine whether word exists
        im the grid
        @param row: int. Row num
        @param col: int. Column num
        @param pos: int. Current Nth letter in the word being searched
        @param my_word: string. Letters found thus far that matches our word
        @return is_found: bool. Flag signifying we have found our word
        """
        is_found = False

        if self.grid[row][col] == self.word[pos]:
            my_word += self.grid[row][col]
            pos += 1

        if self.word == my_word:
            is_found = True

        elif (self.word != my_word) and (len(my_word) > 0):

            # word is partially constructed
            # look at adjacent cells for next letter
            if (col+1 <= self.size[1]) and (self.grid[row][col+1] == self.word[pos]) and (not is_found):
                # look at right cell
                is_found = self.search_word(row=row, col=col+1, pos=pos, my_word=my_word)

            if (col-1 >= 0) and (self.grid[row][col-1] == self.word[pos]) and (not is_found):
                # look at left cell
                is_found = self.search_word(row=row, col=col-1, pos=pos, my_word=my_word)

            if (row+1 <= self.size[0]) and (self.grid[row+1][col] == self.word[pos]) and (not is_found):
                # look at cell below
                is_found = self.search_word(row=row+1, col=col, pos=pos, my_word=my_word)

            if (row-1 >= 0) and (self.grid[row-1][col] == self.word[pos]) and (not is_found):
                # look at cell above
                is_found = self.search_word(row=row-1, col=col, pos=pos, my_word=my_word)

        # word is not constructed yet so continue
        # searching the grid, top-bottom left-right
        if is_found is False:
            if col+1 > self.size[1]:
                if row+1 > self.size[0]:
                    # searched all cells. Word DNE
                    print('>>> Word "{}" cannot be found in grid.'.format(self.word))
                else:
                    # move to next row
                    is_found = self.search_word(row=row+1, col=0, pos=0, my_word='')
            else:
                # move to next column
                is_found = self.search_word(row=row, col=col+1, pos=0, my_word='')

        return is_found

# Test cases

grid = [['r', 'a']
        , ['s', 't']]
assert FindWord2D(grid, 'elephant').search_word(0, 0, 0, '') is False

grid = [['c', 'r', 'b', 'l']
        , ['g', 'g', 'e', 'f']
        , ['d', 'c', 'r', 'a']
        , ['k', 'm', 's', 't']]
assert FindWord2D(grid, 'star').search_word(0, 0, 0, '') is True

grid = [['c', 'r', 'b', 'l', 'e']
        , ['g', 'g', 'e', 'f', 'u']
        , ['s', 't', 'r', 'a', 'z']
        , ['k', 'a', 's', 't', 'a']
        , ['t', 'v', 'h', 'g', 'r']]
assert FindWord2D(grid, 'star').search_word(0, 0, 0, '') is True

grid = [['c', 'r', 'b', 'l', 'e']
        , ['c', 'r', 'a', 't', 's']
        , ['k', 'a', 's', 't', 'a']]
assert FindWord2D(grid, 'star').search_word(0, 0, 0, '') is True
