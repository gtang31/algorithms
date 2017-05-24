"""
Implementation of a singly linked list. A Linked list is a data structure where
each element in the list is a node that contains the data and a pointer to the
next node. The last node in a linked list points to a null. Linked lists are
very similar to lists except for the following:
Pros:
- Linked list have easy insertion/deletion.
- Linked list have dynamic sizes.
Cons:
- Linked lists take up more space due to nodes storing pointers to next element.
- No random access. Must traverse each node sequentially to find specific value.
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
    """
    Linear data structure consisting of Node object(s)
    """
    def __init__(self):
        self.head = None
        self.tail = self.head

    def append(self, value):
        """
        Appends a new node the end of the linked list by setting it equal
        to the tail node.
        Time complexity is O(1)
        @param value: can be Node object or int/str/etc.
        """
        if not self.head:
            if isinstance(value, Node):
                self.head = value
            else:
                self.head = Node(value)
            self.tail = self.head
        else:
            if isinstance(value, Node):
                self.tail.next = value
            else:
                self.tail.next = Node(value)
            self.tail = self.tail.next

    def delete(self, value):
        """
        delete first node occurence containing given specified value.
        Worst-case time complexity is O(n)
        """
        node = self.head
        if node:
            if node.value == value:
                # handle case when we are deleting head node
                self.head = node.next
                return
        while node.next is not None:
            prev = node
            if node.next.value == value:
                if node.next is self.tail:
                    # make sure we update the tail node
                    self.tail = node
                # delete node
                prev.next = node.next.next
                return
            else:
                node = node.next
        return

    def pprint(self):
        """
        pretty prints the linked list vertically on STD
        """
        node = self.head
        while node:
            if node is self.head:
                print('+--|--+{}'.format('HEAD'))
            else:
                print('+--|--+')
            print('|{:05}|'.format(node.value))
            if node is self.tail:
                print('+--|--+{}'.format('TAIL'))
            else:
                print('+--|--+')
            print('   o   ')
            node = node.next
        else:
            print('+--|--+')
            print('|  X  |')
            print('+-----+')
