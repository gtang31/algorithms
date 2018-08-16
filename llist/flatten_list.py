"""
Create an iterator that has the `next` and `has_next` methods that will flatten a nested list data.
The list may be nested on many levels. The iterator will be called via a `flateen_list` function.
"""
from stack import Stack


class NestedIterator(object):

    def __init__(self, nested_list):
        """
        Initialize your data structure here.
        :type nested_list: List[NestedInteger]
        """
        self._stack = Stack()
        self._stack.push(nested_list)

    def next(self):
        """
        Assume that the top element in the stack will
        always be an integer
        :rtype: int
        """
        return self._stack.pop()

    def has_next(self):
        """
        The idea is to ensure that the top element in the stack
        will always be an integer before returning a value for this method.
        This will simplify our `next` method. We handle putting items back onto
        the stack here as well.
        :rtype: bool
        """
        while not self._stack.is_empty():
            if isinstance(self._stack.peek(), int):
                # the first element on the stack is an integer
                return True
            else:
                # the first element is a list, therefore we will need to
                # put the list's elements into the stack. In effect, this is
                # the  `flattening` process
                for i in self._stack.pop()[::-1]:
                    self._stack.push(i)
        return False


def flatten_list(nested_list):
    # NestedIterator object will be instantiated and called as such:
    i, v = NestedIterator(nested_list), []
    while i.has_next():
        n = i.next()
        v.append(n)
    return v


assert(flatten_list([[1,1],2,[1,1]]) == [1,1,2,1,1])
assert(flatten_list([1,[4,[6,2,[8,[9]]]]]) == [1,4,6,2,8,9])
assert(flatten_list([[[[]]]]) == [])
assert(flatten_list([[[[]],[]]]) == [])
