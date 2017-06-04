"""
Implementation of a binary search tree. The binary search tree is constructed
from a sorted linked list
"""
from llist.linkedlist import LinkedList
from tree.btree import Node
__author__ = 'Gary Tang'


class BinarySearchTree(object):
    """
    Binary search tree is essentially a binary tree where a node's left
    descendents all have smaller value and right descendents are larger value.
    """
    def __init__(self, from_list=[]):
        """
        We need to sort the linked list first before we can construct the BST
        """
        ll = LinkedList(from_list)
        self.root = self._construct_bst(ll.head)

    def _construct_bst(self, root):
        """
        we perform an operation that is similar to binary search to construct
        the binary search tree
        @return head: Root of the binary search tree
        """
        if root is None:
            return None
        if root.next is None:
            return Node(root.value)
        slow = root
        fast = root.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head = Node(slow.next.value)
        right = slow.next.next  # right half of the linked list
        slow.next = None
        head.left = self._construct_bst(root)
        head.right = self._construct_bst(right)
        return head

    def traverse(self):
        """
        this method is mostly used to verify that the binary tree was
        constructed properly. Uses in-order traversal to print the tree
        """
        traversal = []

        def in_order(root):
            if root is None:
                return None
            in_order(root.left)
            traversal.append(root.value)
            in_order(root.right)
        in_order(self.root)
        return traversal


# test cases
bst = BinarySearchTree([1, 2, 3, 4, 5, 6, 7])
assert bst.traverse() == [1, 2, 3, 4, 5, 6, 7]

bst = BinarySearchTree([1, 2, 3, 4])
assert bst.traverse() == [1, 2, 3, 4]

bst = BinarySearchTree([1])
assert bst.traverse() == [1]

bst = BinarySearchTree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
assert bst.traverse() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

bst = BinarySearchTree([])
assert bst.traverse() == []
