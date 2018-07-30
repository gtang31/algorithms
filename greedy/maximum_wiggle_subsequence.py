"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative.
The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence.
A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence,
leaving the remaining elements in their original order.
"""


def wiggle_length(self, nums):
    """
    Greedy approach, keep track of number of sequential maximum and minimum elements in nums
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 1:
        return len(nums)
    wiggle = [nums[1]-nums[0]]
    if wiggle == [0]:
        return 1

    for idx in range(1, len(nums)):
        diff = nums[idx]-nums[idx-1]
        if (not wiggle and diff != 0) or (diff > 0 and wiggle[-1] < 0) or (diff < 0 and wiggle[-1] > 0):
            wiggle.append(diff)

    return len(wiggle)+1



assert(wiggle_length([1, 7, 4, 9, 2, 5]) == 6)
assert(wiggle_length([3, 3, 3, 2, 5]) == 3)
assert(wiggle_length([1, 4, 7, 2, 5]) == 4)
assert(wiggle_length([1, 7, 4, 5, 5]) == 4)
assert(wiggle_length([]) == 0)
assert(wiggle_length([0, 0]) == 0)
assert(wiggle_length([1]) == 1)
