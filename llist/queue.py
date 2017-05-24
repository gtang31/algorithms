"""
Implementation of a stack. The stack is a FIFO (first in, first out) data
structure that supports the following operation/methods:
- enqueue
- dequeue
- size
- is_empty
This script implements a stack using a singly linked list.
"""
from linkedlist import LinkedList
__author__ = "Gary Tang"


class Queue(object):
    """
    The queue should add and remove items with O(1) time complexity. In this
    implementation we will only use LinkedList methods and we add to the head
    node and remove from the tail node.
    """
    def __init__(self):
        self._queue = LinkedList()
        self._size = 0

    def enqueue(self, val):
        """
        add item to the back of the queue
        """
        self._size += 1
        self._queue.append(val)

    def dequeue(self):
        """
        remove item from front of the queue
        """
        if self.is_empty():
            raise Exception('Queue is already empty')
        self._size -= 1
        node = self._queue.head
        self._queue.head = self._queue.head.next
        return node

    def is_empty(self):
        return self._queue.head is None

    def size(self):
        return self._size
