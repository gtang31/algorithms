"""
Detect cycle in a linked list and return the head of the cycle. We use a slow
and fast pointer traversing the linked list, if the fast pointer reaches a null
then no cycle exists. Otherwise the slow and fast pointer will eventually meet.
"""
from llist.linkedlist import Node
__author__ = "Gary Tang"


def has_cycle(head):
    """
    @param head: Head node of linked list
    @return node: Node of beginning of cycle. If no cycle, return None
    """
    if head is None or head.next is None:
        return None
    slow = Node(-1)
    slow.next = head
    fast = head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            # cycle was found
            break
    else:
        # ll has no cycle
        return None

    # To find the beginning of the ll cycle, we must figure out the length k of
    # the cycle. Then we have 2 pointers at the head and at the k+1 node and
    # iterate, the pointers will eventually meet at the cycle head.
    k, slow = 1, slow.next
    while slow is not fast:
        slow = slow.next
        k += 1

    # set new pointers
    new = kth = head
    for i in xrange(k):
        kth = kth.next

    while new is not kth:
        # iterate until both pointers meet at the cycle head3
        new = new.next
        kth = kth.next
    return new


# test case
#    _____________
#    |           |
# 1->2->3->4->5->6
cycle_head = ptr = Node(2)
tail = Node(6)
tail.next = cycle_head
head = Node(1)
head.next = cycle_head
a = Node(3)
b = Node(4)
c = Node(5)
ptr.next = a
ptr = ptr.next
ptr.next = b
ptr = ptr.next
ptr.next = c
ptr = ptr.next
ptr.next = tail
assert has_cycle(head) is cycle_head

# 1->2->3->4->5->6->X
head = ptr = Node(1)
ptr.next = Node(2)
ptr = ptr.next
ptr.next = Node(3)
ptr = ptr.next
ptr.next = Node(4)
ptr = ptr.next
ptr.next = Node(5)
ptr = ptr.next
assert has_cycle(head) is None

#             ____
#             |  |
# 1->2->3->4->5->6
cycle_head = Node(5)
tail = Node(6)
tail.next = cycle_head
cycle_head.next = tail
head = ptr = Node(1)
a = Node(2)
b = Node(3)
c = Node(4)
ptr.next = a
ptr = ptr.next
ptr.next = b
ptr = ptr.next
ptr.next = c
ptr = ptr.next
ptr.next = cycle_head
assert has_cycle(head) is cycle_head
