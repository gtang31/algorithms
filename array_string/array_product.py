"""
Given an array nums of n integers where n > 1,  return an array output such that
output[i] is equal to the product of all the elements of nums except nums[i].

Note: Please solve it without division and in O(n).
Solve with constant space complexity?
"""


def product_except_self(nums):
    """
    Calculate two pass. First pass is the cumulative product starting
    from the left, second pass is from right.
    """
    if len(nums) < 2:
        return nums

    forward = nums[:]
    # first pass
    for i in range(1, len(forward)):
        forward[i] = forward[i-1]*forward[i]
    print(forward)

    # second pass, reversed
    for j in range(len(nums)-2, -1, -1):
        nums[j] = nums[j+1]*nums[j]
    print(nums)

    output = forward[:]
    for i in range(len(output)):
        if i == 0:
            output[i] = nums[i+1]
        elif i == len(output)-1:
            output[i] = forward[i-1]
        else:
            output[i] = forward[i-1]*nums[i+1]

    return output


assert(product_except_self([]) == [])
assert(product_except_self([1]) == [1])
assert(product_except_self([2,4,6,8,10]) == [1920,960,640,480,384])
assert(product_except_self([1,2,3,4]) == [24,12,8,6])
