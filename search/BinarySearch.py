"""
Assumes input array is already sorted. Otherwise
search will not be correct. Recursively halves array
until it is of size 1. Compares against our target T.
Run time for this algorithm should be O(logN)
"""
__author__ = "Gary Tang"


def binary_search(array, T):
    """
    @param array: list[int]
    @param T: int
    @return: bool
    """
    if not array:
        return False
    elif len(array) == 1:  # only one element, check if it is our target T
        return array[0] == T

    # calculate midde index and the left/right halves of array
    mid_idx = len(array)/2
    left_half = array[:mid_idx]
    right_half = array[mid_idx:]

    if T < array[mid_idx]:
        return binary_search(left_half, T)
    else:
        return binary_search(right_half, T)

# Test cases
assert binary_search([1,2,3,4,5], 6) == False
assert binary_search([1,2,3,4,5], 4) == True
assert binary_search([], 99) == False
assert binary_search([1,1,3,4,5,5], 5) == True
