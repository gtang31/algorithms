"""
Implementation of a singly linked list. A Linked list is a data structure where
each element in the list is a node that contains the data and a pointer to the
next node. The last node in a linked list points to a null. Linked lists are
very similar to lists except for the following:
Pros:
- Linked list have easy insertion/deletion.
- Linked list have dynamic sizes.
Cons:
- Linked lists take up more space due to nodes storing pointers to next element
- No random access. Must traverse each node sequentially to find a specific value
"""


class Node(object):
    """
    Sub-unit of a linked list. Contains a value and pointer to next node in the
    list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None  # init point to None to signify end of llist


class LinkedList(object):

    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Appends a new node the end of the linked list
        """
        if not self.head:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next:
                # we will need to loop thru all nodes to reach the tail
                temp = temp.next
            temp.next = Node(value)

    def delete(self, value):
        """
        delete first node occurence containing given specified value
        """
        node = self.head
        if node:
            if node.value == value:
                self.head = node.next
                return
        while node.next is not None:
            prev = node
            if node.next.value == value:
                prev.next = node.next.next
                return
            else:
                node = node.next
        return

    def pprint(self):
        """
        pretty prints a linked list vertically on STD
        """
        node = self.head
        while node:
            print('+--|--+')
            print('|{:05}|'.format(node.value))
            print('+--|--+')
            print('   o   ')
            node = node.next
        else:
            print('+--|--+')
            print('|  X  |')
            print('+-----+')
