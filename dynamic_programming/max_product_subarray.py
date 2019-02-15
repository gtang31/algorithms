"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""
import pdb


def max_product(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    # curr variable represents the positive product up to current idx position
    # running variable represents the running product that includes negative values
    # we reset both variables every time we encounter 0
    curr = running = nums[0]
    for idx in range(1, len(nums)):
        # pdb.set_trace()
        if nums[idx] == 0:
            # reset, start new subarray product
            curr = running = 0
            continue

        if (nums[idx] > 0) and (curr <= 0):
            curr = nums[idx]  # init
        elif (nums[idx] > 0) and (curr > 0):
            curr *= nums[idx] # update
        else:
            curr = 0  # reset if we hit a negative value

        if (running == 0):
            running = nums[idx]  # init
        else:
            running *= nums[idx] # update

        # update current position in nums with max value
        nums[idx] = max(running, curr)

    print(nums)
    return(max(nums))


# nums = [-1, 6, 2, 0, 3, -4]
# assert(max_product(nums) == 12)

# nums = [-1, 6, 2, 1, 3, -4]
# assert(max_product(nums) == 144)

# nums = [-2, 0, -1]
# assert(max_product(nums) == 0)

# nums = [2, 3, -2, 4]
# assert(max_product(nums) == 6)

nums = [2, -2, -3, -5, 4]
assert(max_product(nums) == 60)

# nums = [-3]
# assert(max_product(nums) == -3)

nums = [2,-5,-2,-4,3]
assert(max_product(nums) == 24)

