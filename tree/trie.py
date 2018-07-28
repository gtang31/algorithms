"""
Implement the Trie data structure. A Trie is essentially a special-case of the
tree data structure, where each node in the trie contains 26 child, one for
each letter in the alphabet
"""
from tree.btree import BTree, Node
__author__ = 'Gary Tang'


class Trie(Tree):

    def __init__(self):
        # in databases, K should be a multiple of the hardware page size
        super(Trie, self).__init__(K=32, from_list=['ROOT'])

    def insert(self, word, node=None):
        """
        @param word. String to insert into the Trie
        """
        if not word:
            # base case, we have inserted the entire word
            return
        if node is None:
            # default call to method
            node = self.root
        for child in node.children:
            if child.value == word[0]:
                # prefix up to this letter was found
                next_node = child
                break
        else:
            node.children.append(Node(word[0]))
            next_node = node.children[-1]
        self.insert(word[1:], next_node)

    def search(self, prefix, node=None):
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
        return self.search(prefix[1:], next_node) and True
