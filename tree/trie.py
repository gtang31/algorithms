"""
Implement the Trie data structure. A Trie is essentially a special-case of the
tree data structure, where each node in the trie contains up to 26 children, one for
each letter in the alphabet. A word is complete if it is followed by an asterisk(*).
"""
from tree.btree import BTree, Node
__author__ = 'Gary Tang'


class Trie(object):

    def __init__(self):

        self.root = Node("ROOT")

    def insert(self, word, node=None):
        """
        @param word. String to insert into the Trie
        """
        if not word:
            # base case, we have inserted the entire word
            node.children.append(Node('*'))
            return

        if node is None:
            # set default node to root. Usually call by user
            node = self.root

        for child in node.children:
            if child.value == word[0]:
                # prefix up to this letter was found
                # move to next child
                next_node = child
                break
        else:
            # prefix not found, so add new child
            node.children.append(Node(word[0]))
            next_node = node.children[-1]

        self.insert(word[1:], next_node)

    def search(self, word, node=None):
        """
        check whether a string exists in the trie
        @para word: String.
        """
        if not word:
            for child in node.children:
                if child.value == '*':
                    # word exists
                    return True
            return False

        if not node:
            node = self.root

        for child in node.children:
            if word[0] == child.value:
                break
        else:
            return False

        return self.search(word[1:], child)

    def startswith(self, prefix, node=None):
        """
        @param prefix. string. Search whether the trie contains given prefix.
        @return bool
        """
        if not prefix:
            return True

        if node is None:
            node = self.root

        for child in node.children:
            if prefix[0] == child.value:
                next_node = child
                break
        else:
            return False

        return self.startswith(prefix[1:], next_node) and True


if __name__ == '__main__':
    # test cases.
    trie = Trie()
    trie.insert('alphabet')
    trie.insert('alphanumeric')
    trie.insert('alpha')
    assert(trie.search('alphabet') == True)
    assert(trie.search('alphanumeric') == True)
    assert(trie.search('alpha') == True)
    assert(trie.startswith('alph') == True)
    assert(trie.startswith('beta') == False)
    trie.insert('alpine')
    assert(trie.search('alpine') == True)
    assert(trie.startswith('alpine') == True)
    assert(trie.search('alps') == False)
