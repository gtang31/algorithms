"""
Prints a list of keys that represents the order in which each node was visited
in a tree. '#' represents an empty node. If a list[list[int]] is returned, this
is highlight the number of nodes at a particular level.

Implementation of different traversal methods:
1.) Pre-Order
2.) In-Order
3.) Post-Order
4.) ZigZag
5.) Level-Order
"""
from llist.queue import Queue
from tree.binarytree import BinaryTree, Node as TreeNode
from tree.bstree import BinarySearchTree
from tree.heap import Heap
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
        q = Queue()
        q.enqueue((node, level))
        while not q.is_empty():
            node, level = q.dequeue()
            if node is not None:

                # index in traversal list represents the level in the binary tree
                if len(traversal)-1 < level:
                    traversal.append([node.value])
                else:
                    traversal[level].append(node.value)
                q.enqueue((node.left, level+1))
                q.enqueue((node.right, level+1))
        return traversal


# test cases
# BST
bst = BinarySearchTree([4, 8, 1, 2, 5, 6, 0])
assert(Traversal().level_order(bst.root) == [[4], [1, 6], [0, 2, 5, 8]])

bst = BinarySearchTree([4, 8, 1, 2, 5, 6, 0])
assert(Traversal().in_order(bst.root) == [0, 1, 2, 4, 5, 6, 8])

bst = BinarySearchTree([])
assert(Traversal().level_order(bst.root) == [])

# Binary Trees
t = BinaryTree([1, 2, 3, 4, 5])
assert(Traversal().in_order(t.root) == [4, 2, 5, 1, 3])

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

# Heaps
min_heap = Heap([5,3,6,7,1,9])
t = BinaryTree(min_heap._heap_list[1:])
assert(Traversal().level_order(t.root) == [[1], [3, 6], [7, 5, 9]])

min_heap.insert(4)
t = BinaryTree(min_heap._heap_list[1:])
assert(Traversal().level_order(t.root) == [[1], [3, 4], [7, 5, 9, 6]])

assert(min_heap.extract() == 1)
t = BinaryTree(min_heap._heap_list[1:])
assert(Traversal().level_order(t.root) == [[3], [5, 4], [7, 6, 9]])

max_heap = Heap([5,3,6,7,1,9], 'max')
t = BinaryTree(max_heap._heap_list[1:])
assert(Traversal().level_order(t.root) == [[9], [6, 7], [3, 1, 5]])

max_heap.insert(4)
t = BinaryTree(max_heap._heap_list[1:])
assert(Traversal().level_order(t.root) == [[9], [6, 7], [3, 1, 5, 4]])

assert(max_heap.extract() == 9)
t = BinaryTree(max_heap._heap_list[1:])
# print(Traversal().level_order(t.root))
assert(Traversal().level_order(t.root) == [[7], [6, 5], [3, 1, 4]])

assert(max_heap.extract() == 7)
assert(max_heap.extract() == 6)
t = BinaryTree(max_heap._heap_list[1:])
assert(Traversal().level_order(t.root) == [[5], [4, 1], [3]])

h=Heap([6,4,5])
assert(h.extract() == 4)
assert(h.extract() == 5)
assert(h.extract() == 6)
