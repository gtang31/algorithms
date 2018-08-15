"""
Given a sorted array, it is rotated at an index K that is unknown to you.
Search for a `target` value within the rotated array in O(logn) time and
return its index. If DNE, return -1.
"""


def search(nums, target):
    """
    The idea is to use a modified binary search. Whenever we split the
    rotated into it left/right components, we need to compare the values
    and the zeroth and middle index. Based on the comparison, we decide
    either to search left or right half.
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    left, right = 0, len(nums)
    while left < right:
        mid = (right-left)//2+left
        if nums[mid] == target:
            return mid
        elif (nums[left] <= target) and (nums[mid] < target):
            # check for pivot
            if nums[left] > nums[mid]:
                # there was pivot
                # consider case ([4,5,6,1,2,3] , 6)
                right = mid
            else:
                left = mid+1
        elif (nums[left] <= target) and (nums[mid] > target):
            # target is in left half. No pivot
            right = mid
        elif (nums[left] >= target) and (nums[mid] < target):
            # target is in right half. pivot has happened
            left = mid+1
        elif (nums[left] >= target) and (nums[mid] > target):
            # check for pivot
            if nums[left] > nums[mid]:
                # there was pivot
                # consider case ([6,0,1,2,3,4,5] , 1)
                right = mid
            else:
                left = mid+1
    return -1


assert(search([4,5,6,7,0,1,2], 0) == 4)
assert(search([8,9,2,3,4], 9) == 1)
assert(search([7,8,1,2,3,4,5,6], 2) == 3)
assert(search([4,5,6,7,0,1,2], 1) == 5)
assert(search([3,4,5,6,7,0,1,2], 2) == 7)
assert(search([4,5,6,7,0,1,2], 3) == -1)

