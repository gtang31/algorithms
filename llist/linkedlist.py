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
    Linear data structure consisting of Node object(s). This is a singly linked
    list where each node in the list only points to the next node
    """
    def __init__(self, from_list=[]):
        self.head = self.tail = None  # init

        if isinstance(from_list, Node):
            # create a linked list from a Node object
            self.head = self.tail = from_list
            from_list = from_list.next
            while from_list is not None:
                self.tail = from_list
                from_list = from_list.next

        elif isinstance(from_list, list) and from_list:
            # construct linked list from an array (list) object
            self.tail = self.head = Node(from_list[0])
            for i in range(1, len(from_list)):
                self.tail.next = Node(from_list[i])
                self.tail = self.tail.next

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

    def reverse(self):
        """
        reverse the order of nodes in the linked list
        """
        self.tail = self.head
        prev = None
        current = self.head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    def pprint(self):
        """
        pretty prints the linked list vertically on STD
        """
        node = self.head
        ll = ''
        while node:
            if node is self.head:
                ll += '+--|--+{}\n'.format('HEAD')
            else:
                ll += '+--|--+\n'
            ll += '|{:05}|\n'.format(node.value)
            if node is self.tail:
                ll += '+-----+{}\n'.format('TAIL')
            node = node.next
        else:
            ll += '+--|--+\n'
            ll += '|  X  |\n'
            ll += '+-----+'
        print(ll)


def chain_nodes(_list):
    """
    this function is mostly used for testing
    """
    head = temp = Node(_list[0])
    if len(_list) > 1:
        for i in range(1, len(_list)):
            temp.next = Node(_list[i])
            temp = temp.next
    return head

def print_chain(node):
    ret = []
    while node:
        ret.append(str(node.value))
        node = node.next
    print('->'.join(ret))


