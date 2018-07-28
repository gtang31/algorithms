"""
Given two binary trees, P and Q, find whether Q is a subtree of P. We will need
to check for the existence of subtree Q for every node we visit in P.
"""
from tree.binarytree import BinaryTree
__author__ = 'Gary Tang'


def is_subtree(p, q):
    """
    For each node visited, check whether its descendents contain the subtree.
    O(P*Q) time complexity
    @param p. Root of P
    @param q: Root of Q
    @return bool
    """
    def subtree_exist(p, q):
        """
        helper function. This function does the actual checking for a subtree
        """
        if (p is None) and (q is None):
            return True
        if (p is None) or (q is None):
            # mis-match
            return False
        return p.value == q.value and subtree_exist(p.left, q.left) and subtree_exist(p.right, q.right)

    if p is None:
        # None node cannot contain a subtree
        return False
    if subtree_exist(p, q):
        # we found a subtree match
        return True
    if (is_subtree(p.left, q)) or (is_subtree(p.right, q)):
        # subtree was already found in either left of right descendents
        return True
    return False


# test cases
P = BinaryTree([3, 4, 5, 1, 2])
Q = BinaryTree([4, 1, 2])
assert is_subtree(P.root, Q.root) is True

P = BinaryTree([3, 4, 5, 1, 2, None, None, None, None, 0])
Q = BinaryTree([4, 1, 2])
assert is_subtree(P.root, Q.root) is False

P = BinaryTree([3, 4, 5, 1, 2, None, None, None, None, 0, 4, None, None, 1, 2])
Q = BinaryTree([4, 1, 2])
assert is_subtree(P.root, Q.root) is True

P = BinaryTree([3, 4, 5, 1, 2, None, None, None, None, 0, 4, None, None, 2])
Q = BinaryTree([4, 1, 2])
assert is_subtree(P.root, Q.root) is False

P = BinaryTree([3, 4, 5, 1, 2, 4, 2, None, None, 4, 2, 1, 2])
Q = BinaryTree([4, 1, 2])
assert is_subtree(P.root, Q.root) is True
