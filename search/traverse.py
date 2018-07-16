"""
Implementation of different traversal methods:
1.) Pre-Order
2.) In-Order
3.) Post-Order
4.) ZigZag
"""
from queue import Queue
from tree.btree import Node as TreeNode
from tree.btree import BinaryTree
__author__ = 'Gary Tang'


class Traversal(object):

    def zig_zag(self, root):
        """
        zigzag level order traversal of its nodes' values.
        IE, from left to right, then right to left for the next level and alternate between.
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        output, stack, temp = [[root.value]], [(root, 0)], []
        while stack:
            node, level = stack.pop()
            if node and (level%2 == 0):
                # push right child node onto temp stack first
                temp.append((node.right, level+1))
                temp.append((node.left, level+1))
            elif node and (level%2 == 1):
                # push left child node onto temp stack first
                temp.append((node.left, level+1))
                temp.append((node.right, level+1))
            
            if not stack and temp:
                stack = temp
                output.append([node[0].value for node in temp if node[0] is not None])
                temp = []
        output.pop()  # remove the leaf children
        return output

    def in_order(self, root):
        """
        In-order traversal's order is: left child, parent, right child
        type root: TreeNode
        rtype: List[int]
        """
        traversal = []
        def dfs(node):
            """DFS helper function"""
            if node is None:
                return

            dfs(node.left)
            traversal.append(node.value)
            dfs(node.right)
        dfs(root)
        return traversal

    def pre_order(self, root):
        """
        Pre-order traversal's order is: parent, left child, right child
        type root: TreeNode
        rtype: List[int]
        """
        traversal = []
        def dfs(node):
            """DFS helper function"""
            if node is None:
                return

            traversal.append(node.value)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return traversal

    def post_order(self, root):
        """
        Post-order traversal's order is: left child, right child, parent
        type root: TreeNode
        rtype: List[int]
        """
        traversal = []
        def dfs(node):
            """DFS helper function"""
            if node is None:
                return

            dfs(node.left)
            dfs(node.right)
            traversal.append(node.value)
        dfs(root)
        return traversal

    def level_order(self, node, level=0):
        """
        Use BFS to display level order traversal: parent, left child, right child
        type node: TreeNode
        rtype: List[List[int]]
        """
        traversal = []
        if not node:
            return traversal
        q = Queue(-1)  # define infinite size
        q.put((node, level))
        while not q.empty():
            node, level = q.get(block=False, timeout=0)
            if node is not None:
                if len(traversal)-1 < level:
                    traversal.append([node.value])
                else:
                    traversal[level].append(node.value)
                q.put((node.left, level+1))
                q.put((node.right, level+1))
        return traversal



t = BinaryTree([3, 9, 20, None, None, 15, 7])
assert(Traversal().zig_zag(t.root) == [[3],[20,9],[15,7]])

t = BinaryTree([1,2,3,4,5,6,7,8,9,10,11])
assert(Traversal().zig_zag(t.root) == [[1], [3,2], [4,5,6,7], [11,10,9,8]])

t = BinaryTree([])
assert(Traversal().zig_zag(t.root) == [])

t = BinaryTree([1, 2, 3, 4, 5])
assert(Traversal().pre_order(t.root) == [1, 2, 4, 5, 3])

t = BinaryTree([1, 2, 3, 4, 5])
assert(Traversal().post_order(t.root) == [4, 5, 2, 3, 1])

t = BinaryTree([1, 2, 3, 4, 5, 6, None, None, 7, 8])
assert(Traversal().level_order(t.root) == [[1], [2, 3], [4, 5 ,6], [7, 8]])
