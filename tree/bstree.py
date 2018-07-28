"""
Implementation of a binary search tree. The binary search tree is constructed
from a sorted linked list
"""
from llist.linkedlist import LinkedList
from llist.ll_sort import merge_sort
from tree.binarytree import Node
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
        ll = LinkedList(merge_sort(ll.head))
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
