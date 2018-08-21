"""
Given two linked lists, in reverse order, add them together.
1->2->3
4->5
Equals
5->7->3

 321
+ 54
----
 375
"""
from linkedlist import Node, chain_nodes, print_chain


def add(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = 0
    head = l1
    while l1 and l2:
        prev1, prev2 = l1, l2
        temp = l1.value + l2.value + carry
        carry = temp//10
        l1.value = temp%10
        l1 = l1.next
        l2 = l2.next

    if (l1 is None) and l2:
        # len(l2) > len(l1)
        prev1.next = l2
        prev1 = prev1.next
    elif (l2 is None) and l1:
        # len(l1) > len(l2)
        prev1 = prev1.next
    else:
        # len(l1) == len(l2), check for a carry
        if carry == 1:
            prev1.next = Node(carry)
            carry = 0

    while carry == 1:
        temp = prev1.value + carry
        prev1.value = temp%10
        if (prev1.next is None) and (temp >= 10):
            prev1.next = Node(carry)
            break
        carry = temp//10
        prev1 = prev1.next

    return head


# test cases
l1 = chain_nodes([9,9,9,9])
l2 = chain_nodes([9])
print_chain(add(l1, l2))

l1 = chain_nodes([5])
l2 = chain_nodes([5])
print_chain(add(l1, l2))

l1 = chain_nodes([2])
l2 = chain_nodes([8,1])
print_chain(add(l1, l2))
