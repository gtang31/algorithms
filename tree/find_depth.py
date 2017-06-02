"""
Find depth of a binary tree. We implement the solution using recursion. We can
achieve the same solution using iteration.
"""
from tree.btree import BinaryTree
__author__ = 'Gary Tang'


def min_depth(node):
    """
    The minimum depth of a tree is the shortest branch from root to a leaf
    """
    if not node:
        return 0
    elif (not node.left) and (not node.right):
        # found leaf
        return 1
    elif not node.left:
        # if the root has only 1 child, this prevents the minimum depth from
        # equaling zero
        return min_depth(node.right) + 1
    elif not node.right:
        return min_depth(node.left) + 1
    return min(min_depth(node.left), min_depth(node.right)) + 1


def max_depth(node):
    """
    The maximum depth of a tree is the longest branch from root to a leaf
    """
    if not node:
        return 0
    return max(max_depth(node.left), max_depth(node.right)) + 1


# test cases
P = BinaryTree([3, 4, 5, 1, 2])
assert min_depth(P.root) == 2
assert max_depth(P.root) == 3

P = BinaryTree([3, 4, 5, 1, 2, None, None, None, None, 0])
assert min_depth(P.root) == 2
assert max_depth(P.root) == 4

P = BinaryTree([3, 4, 5, 1, 2, None, None, None, None, 0, 4, None, None, 1, 2])
assert min_depth(P.root) == 2
assert max_depth(P.root) == 5

P = BinaryTree([3, 4, 5, 1, 2, 4, 2, None, None, 4, 2, 1, 2])
assert min_depth(P.root) == 3
assert max_depth(P.root) == 4

P = BinaryTree([1, 2])
assert min_depth(P.root) == 2
assert max_depth(P.root) == 2
