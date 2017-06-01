"""
Implementation of a binary tree. The binary tree is constructed using BFS to
populate each node from an input list
"""
from llist.linkedlist import LinkedList
from llist.queue import Queue
__author__ = 'Gary Tang'


class Node(object):
    """
    Binary tree nodes contains only left and right childrens
    """
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


class BinaryTree(object):
    """
    A binary tree consists of at most one root node. Each node can have at most
    two children
    """
    def __init__(self, from_list=[]):
        """
        Construct the binary tree from a linked list. We will need to use a
        queue to keep track of the child nodes
        """
        ll = LinkedList(from_list)
        if ll.head:
            self.root = Node(ll.head.value)
            _q = Queue()
            _q.enqueue(self.root)
            ll.head = ll.head.next
        else:
            self.root = None
        while ll.head:
            node = _q.dequeue()
            # populate left child and enqueue it
            node.left = Node(ll.head.value)
            _q.enqueue(node.left)
            if ll.head:
                # populate right child
                node.right = Node(ll.head.value)
                _q.enqueue(node.right)
            ll.head = ll.head.next

    def traverse(self):
        """
        this method is mostly used to verify that the binary tree was
        constructed properly. Uses pre-order traversal to print the tree
        """
        def pre_order(root):
            if not root:
                return None
            print root.value
            pre_order(root.left)
            pre_order(root.right)
        return pre_order(self.root)


class BST(object):
    """
    Binary search tree
    """
    def __init__(self, from_list=[]):
        pass
