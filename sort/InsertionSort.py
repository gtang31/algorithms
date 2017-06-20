"""
Performs insertion sort. This algorithm's performance is
O(n^2). Can be further improved to O(nlogn) using a
binary insertion method.
"""
__author__ = "Gary Tang"


def insert_sort(unordered_list):
    if not unordered_list:
        return []

    for ptr in range(1, len(unordered_list)):

        while ptr - 1 >= 0:
            if unordered_list[ptr] < unordered_list[ptr - 1]:
                # swap element into correct position
                unordered_list[ptr], unordered_list[ptr - 1] = unordered_list[ptr - 1], unordered_list[ptr]
            ptr -= 1  # decrement pointer position

    return unordered_list  # return ordered list


def binary_insert_sort(unordered_list):
    # TODO: implement
    pass


assert insert_sort([]) == []
assert insert_sort([3,2,1]) == [1, 2, 3]
assert insert_sort([4,2,3,1,10,6,5,8,9,7,1]) == [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert insert_sort([2,1,1,2,3,1]) == [1, 1, 1, 2, 2, 3]
assert insert_sort([7,99,53,12,60,35,65,2]) == [2, 7, 12, 35, 53, 60, 65, 99]
