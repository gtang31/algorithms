from tree.binarytree import BinaryTree
import pdb


def rob(root):
    def solve(node):
        if not node:
            return 0, 0

        print(node.value)
        pdb.set_trace()
        left, right = solve(node.left), solve(node.right)
        return (node.value + left[1] + right[1]), (max(left) + max(right))
    return max(solve(root))


t = BinaryTree([3, 4, 5, 1, 3, None, 1])
print(rob(t.root))

