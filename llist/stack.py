"""
Implementation of a stack. The stack is a FILO (first in, last out) data
structure that supports the following operation/methods:
- push
- pop
- peek
- is_empty
This script implements a stack using a singly linked list.
"""
from LinkedList import LinkedList, Node


class Stack(object):
    """
    The stack should add and remove items with O(1) time complexity. In this
    implementation we will only use LinkedList methods and we add/remove from
    only the head node this is due to how the linked list is implemented; since
    popping from the tail node would require O(n) time complexity
    """
    def __init__(self):
        self.stack = LinkedList()

    def push(self, val):
        """
        push an item onto the top of the stack
        @param val: item to push onto the stack
        """
        node = Node(val)
        node.next = self.stack.head
        self.stack.head = node

    def pop(self):
        """
        remove the item at the top of the stack
        @return node: node object
        """
        if not self.stack.head:
            raise Exception('Stack is already empty.')
        node = self.stack.head
        self.stack.head = self.stack.head.next
        return node

    def peek(self):
        """
        check value of item at the top of the stack
        @return: value of tail node
        """
        if not self.stack.head:
            raise Exception('Stack is already empty.')
        return self.stack.head.value

    def is_empty(self):
        """
        check if there are any items in the stack
        @return bool: if the head is None, then that means the ll is empty
        """
        return self.stack.head is None