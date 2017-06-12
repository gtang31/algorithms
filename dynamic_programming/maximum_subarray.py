"""
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.
"""
__author__ = 'Gary Tang'


def max_subarray(arr):
    """
    Implement Kadane's algo. We iterate through the array and track the running
    sum. Once we find an element greater than the running sum, we reset it. Then
    we update the global max.
    """
    if not arr:
        return []
    max_sum = curr_sum = arr[0]
    for idx in xrange(1, len(arr)):
        if curr_sum + arr[idx] < arr[idx]:
            # start new continguous array at current idx
            curr_sum = arr[idx]
        else:
            # append to contiguous array
            curr_sum += arr[idx]

        if max_sum < curr_sum:
            max_sum = curr_sum
    return max_sum

assert(max_subarray([-2, -3, -4, -19, -2, -1, -11, -3]) == -1)
assert(max_subarray([-2, -3, 4, -1, -2, 1, 5, -3]) == 7)
assert(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
