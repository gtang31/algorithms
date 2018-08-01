from tree.binarytree import BinaryTree
__author__ = 'Gary Tang'


def is_balanced(root):
    """
    Use bottom-up approach. Once we reach leaves we retreat up the stack space returing 2 values as we go.
    First value is a boolean that tracks whether the tree is balanced up to the current node and its depth.
    :type root: TreeNode
    :rtype: bool
    """
    def _check(node):
        if node is None:
            return True, 0

        balanced, left_depth = check(node.left)
        if not balanced:
            return False, 0

        balanced, right_depth = check(node.right)
        if not balanced:
            return False, 0

        left_depth += 1
        right_depth += 1

        # compare the depth of left vs right subtrees. Ensure they are at least within 1 level of each other
        return abs(left_depth - right_depth) <= 1, max(left_depth, right_depth)

    return _check(root)

t = BinaryTree([3, 9, 20, None, None, 15, 7])
assert(is_balanced(t.root)[0] is True)

t = BinaryTree([1, 2, 2, 3, 3, None, None, 4, 4])
assert(is_balanced(t.root)[0] is False)

t = BinaryTree([0,2,4,1,None,3,-1,5,1,None,6,None,8])
assert(is_balanced(t.root)[0] is False)
