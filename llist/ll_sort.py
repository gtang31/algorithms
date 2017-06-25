"""
Given a linkedlist, sort it into ascending order. We can use the merge sort to
accomplish this in O(nlogn) time.
"""
from llist.linkedlist import Node


def merge_sort(ll_head):
    """
    @param ll_head. Head node of a linked list
    @return ll_head. Head of the the sorted linked list
    use divide and conquer
    """
    if (ll_head is None) or (ll_head.next is None):
        return ll_head
    slow = ll_head
    fast = ll_head.next.next
    while (fast is not None) and (fast.next is not None):
        # split the linked list in half
        slow = slow.next
        fast = fast.next.next

    # init right half of the split ll and set the tail of the left half
    right_head = slow.next
    slow.next = None
    left_half, right_half = merge_sort(ll_head), merge_sort(right_head)

    sorted_ll = Node(-1)  # temp head
    temp = sorted_ll
    # do the merge
    while left_half is not None:
        if right_half is None:
            # reached end of right ll. Or it does not exist
            temp.next = left_half
            break

        # do the sort
        if left_half.value > right_half.value:
            temp.next = right_half
            temp = temp.next
            right_half = right_half.next
        elif left_half.value <= right_half.value:
            temp.next = left_half
            temp = temp.next
            left_half = left_half.next
    else:
        temp.next = right_half

    return sorted_ll.next
