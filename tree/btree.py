"""
Implementation of a K-ary tree. The K-ary tree is a tree where all nodes can
have up to K children. We can implement a K-ary tree from a sorted linked list.
"""
from llist.linkedlist import LinkedList
from llist.queue import Queue
__author__ = 'Gary Tang'


class Node(object):

    def __init__(self, val):
        self.value = val
        self.children = []


class BTree(object):

    def __init__(self, K, from_list=[]):
        """
        K-ary tree is constructed using BFS so when populating children, so we
        need to add `None` in from_list to signify the end of a node's children
        when the number of children for a node is less than K.
        @param K: integer. Maximum number of children a node can have
        @param from_list. List to construct tree from
        """
        ll = LinkedList(from_list)
        if not ll.head:
            self.root = None
        else:
            self.root = Node(ll.head.value)
            _q = Queue()
            _q.enqueue(self.root)
            ll.head = ll.head.next
        while ll.head:
            node = _q.dequeue()
            for i in range(K):
                # iterate through llist for the next K nodes
                if ll.head is None:
                    # tree is fully constructed
                    break
                elif ll.head.value is None:
                    # we reached the stop signal (value is None) for
                    # populating this node's children list
                    ll.head = ll.head.next
                    _q.enqueue(Node(ll.head.value))
                    break
                else:
                    child = Node(ll.head.value)
                    _q.enqueue(child)
                    ll.head = ll.head.next
                    node.children.append(child)
