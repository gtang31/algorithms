"""
Given a tree root, we need to serialize it into a JSON object.
Given a JSON, deserialize it into a Tree object.
This script can be used to pass information about a tree between multiple pieces
of software. For example, visualizing the tree in D3.js
NOTE: trees will be populated with children top-down, left-to-right
"""
import json
from tree.btree import BTree, Node as TNode
from tree.trie import Trie
from tree.binarytree import BinaryTree, Node as BTNode
from tree.bstree import BinarySearchTree
__author__ = 'Gary Tang'


class Codec(object):

    def __init__(self):
        self._data = dict()

    def serialize(self, tree):
        """
        Take the root node of a tree and compress it into a JSON
        @param tree. Tree object
        @return JSON
            ex: {"type": "trie", "data": ["make", "mull", "maven", "making"]}
        """
        self._data['type'] = tree.__name__.lower()

        def recurse(self, tree.root):
            pass

        return json.dumps(self._data)

    def deserialize(self, data):
        """
        Take a JSON object and reconstruct a tree. This is particulary easy
        due to how all my data structures can be created from a list.
        @param data: JSON
            ex: {"type": "btree", "data": [1, 2, null, 4]}
        @return tree. Specified tree object
        """
        data = json.loads(data)
        tree_type = data['type']
        tree_types = ['tree', 'trie', 'binarytree', 'binarysearchtree']
        if tree_type.lower() not in tree_types:
            raise ValueError('Not recognized tree type. See possibilities: {}'.format(tree_types))
        else:
            if tree_type == 'tree':
                # TODO: figure out how many children the user wanted
                pass
            elif tree_type == 'trie':
                trie = Trie()
                for word in data['data']:
                    trie.insert(word)
                return trie
            elif tree_type == 'btree':
                btree = BinaryTree(data['data'])
                return btree
            elif tree_type == 'bstree':
                bstree = BinarySearchTree(data['data'])
                return bstree
