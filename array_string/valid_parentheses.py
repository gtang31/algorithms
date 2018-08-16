"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""
from llist.stack import Stack
__author__ = "Gary Tang"


def is_valid(s):
    opening = {'{', '[', '('}
    stack = Stack()
    for char in s:
        if char in opening:
            stack.push(char)
        else:
            if stack.is_empty():
                # there are no matching open parentheses
                return False

            popped = stack.pop()
            if (popped == '(' and char == ')') or (popped == '[' and char == ']') or (popped == '{' and char == '}'):
                # opening and closing parenthese match up
                continue
            else:
                return False
    return stack.is_empty()


# test cases
s = "()"
assert(is_valid(s) is True)

s = "()[]{}"
assert is_valid(s) is True

s = "(]"
assert(is_valid(s) is False)

s = "([)]"
assert(is_valid(s) is False)

s = "{[]}"
assert(is_valid(s) is True)

s = "("
assert(is_valid(s) is False)

s = "]"
assert(is_valid(s) is False)
