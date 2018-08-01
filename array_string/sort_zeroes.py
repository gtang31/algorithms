"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
import pdb


def move_zeroes(nums):

    if len(nums) < 2:
        return nums

    slow = 0  # increment only after a swap was made
    fast = 1  # always increment, if pointing at nonzero, swap element with slow 
    while fast < len(nums):

        # print(nums)
        # pdb.set_trace()
        if (nums[fast] != 0) and (nums[slow] == 0):
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

        elif nums[slow] != 0:
            slow += 1  # do not swap
            if slow >= fast:  # make sure slow does not overtake fast pointer
                fast += 1
            continue

        fast += 1

    return nums

# test cases
nums = [0,1,0,3,12]
assert(move_zeroes(nums) == [1,3,12,0,0])

nums = [1,0,0,0,3,12]
assert(move_zeroes(nums) == [1,3,12,0,0,0])

nums = [0,0,0,1,0,3,0,5,2,0,12]
assert(move_zeroes(nums) == [1,3,5,2,12,0,0,0,0,0,0])

nums = [2,1]
assert(move_zeroes(nums) == [2,1])

nums = [0,0,0,3,2,1]
assert(move_zeroes(nums) == [3,2,1,0,0,0])

nums = [4,2,4,0,0,3,0,5,1,0]
assert(move_zeroes(nums) == [4,2,4,3,5,1,0,0,0,0])
