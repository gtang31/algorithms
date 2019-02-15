"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


def longest_consecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
        return len(nums)

    nums.sort()
    longest = temp = 0
    for idx in range(1, len(nums)):
        if nums[idx] - nums[idx-1] == 0:
            continue
        elif nums[idx] - nums[idx-1] == 1:
            temp += 1
            longest = max(longest, temp)
        else:
            temp = 0
    return longest+1  # add one because we are starting at index 1


# test cases
assert(longest_consecutive([100, 4, 200, 1, 3, 2]) == 4)
assert(longest_consecutive([100, 4, 200, 1, 3, 2, 2, 4, 5]) == 5)
assert(longest_consecutive([100]) == 1)
assert(longest_consecutive([]) == 0)
assert(longest_consecutive([0, -1]) == 2)
