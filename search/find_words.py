"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.
"""
import pdb


class game(object):

    def find_words(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.board = board
        self.output = []
        for word in words:
            if word in self.output:
                continue
            self.traverse(word)

        return self.output

    def search(self, word, coord):
        # use DFS to check adjacent cells
        row, col = coord

        if not word:
            # found all letters in word
            return True
        elif row < 0 or row == len(self.board) or col < 0 or col == len(self.board[0]):
            # out of bounds
            return False
        elif (coord in self.visited) :
            return False

        # begin search for next letter in the word
        if self.board[row][col] == word[0]:
            self.visited[(row, col)] = self.board[row][col]  # used this cell, cannot revisit!

            # check adjacent cells
            if self.search(word[1:], (row+1, col)):
                return True
            elif self.search(word[1:], (row-1, col)):
                return True
            elif self.search(word[1:], (row, col+1)):
                return True
            elif self.search(word[1:], (row, col-1)):
                return True

            # dead end, remove from visited in case a different path leads to here
            self.visited.pop((row, col), None)
            return False

    def traverse(self, word):
        self.visited = dict()
        # pdb.set_trace()
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == word[0]:
                    if self.search(word, (row, col)):
                        self.output.append(word)
                        return
                    else:
                        self.visited = dict()  # reset visited spaces if we encounter false lead

board = [["a","a"]]
words = ["aaa"]
print(game().find_words(board, words))

words = ["oath", "eat"]
board = [
          ['o','a','a','n'],
          ['e','t','a','e'],
          ['i','h','k','r'],
          ['i','f','l','v']
        ]
print(game().find_words(board, words))

board = [
            ["a","b","c"],
            ["a","e","d"],
            ["a","f","g"]
        ]
words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
print(game().find_words(board, words))

board = [   ["a","b"],
            ["c","d"]
        ]
words = ["cdba"]
print(game().find_words(board, words))

