"""
Given a list of K sorted linked lists. Merge them into one sorted linked list.
"""
from llist.linkedlist import LinkedList
from tree.heap import Heap


def merge_lists(lists):

    node_values = []
    for linked_list in lists:
        while linked_list.head is not None:
            node_values.append(linked_list.head.value)
            linked_list.head = linked_list.head.next

    min_heap = Heap(node_values)  # priority queue
    merged_list = LinkedList()
    while True:
        try:
            _min = min_heap.extract()
            merged_list.append(_min)
        except IndexError:
            break

    return merged_list


# test case
li = [LinkedList([1,4,5]), LinkedList([1,3,4]), LinkedList([2,6])]
ll = merge_lists(li)
ll.pprint()
