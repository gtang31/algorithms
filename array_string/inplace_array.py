"""
Inplace array manipulations with O(1) memory
"""
import pdb


def dedupe_inplace(nums):
    """
    Have two pointers:
        1.) insert pointer - increment after an insertion happens
        2.) "scouting" pointer - travels along nums "looking" for new unseen values
    and a variable that tracks "last seen unique value"
    """
    insert = 0
    moving = 0
    length = 0
    current_value = -1
    while moving < len(nums):
        if nums[moving] > current_value:
            # found an unseen number in our nums list
            # insert new number into position nums[insert]
            # update current_value to new number
            # increment pointers
            current_value = nums[moving]
            length += 1
            nums[insert] = nums[moving]
            insert += 1
        moving += 1
    return nums[:length]


def merge_inplace(nums1, m, nums2, n):
        """
        The idea is to populate from the end of nums1 in descending order while
        keeping track of two pointers that is traversing nums1 and num2 backwards.
        When either index finishes traversing, it becomes more managable to "merge"
        the two arrays.
        Compare nums1[m:-1:-1] to nums2[n:-1:-1] and move larger value to end of nums1
        """
        idx1, idx2, end = m-1, n-1, len(nums1)-1
        while (idx1 >= 0) and (idx2 >= 0):
            if nums1[idx1] > nums2[idx2]:
                nums1[end] = nums1[idx1]
                idx1 -= 1
            elif nums2[idx2] >= nums1[idx1]:
                if idx2 < 0:
                    # check whether we have looped through all elements in nums2
                    # if True, that means everything in nums2 is properly inserted into nums1
                    # add this check for nums2 bc nums2 is shorter than nums1
                    break
                nums1[end] = nums2[idx2]
                idx2 -= 1
            end -= 1
            
        if idx1 == -1:
            # looped through all elements in nums1, therefore every element in num2[:idx2+1]
            # is less than every element in nums1[idx2+1:]
            nums1[0:idx2+1] = nums2[0:idx2+1]
        return nums1


# dedupe test cases
assert(dedupe_inplace([0,0,1,1,1,2,2,3,3,4]) == [0,1,2,3,4])
assert(dedupe_inplace([1,1,2]) == [1,2])
assert(dedupe_inplace([0]) == [0])
assert(dedupe_inplace([]) == [])
assert(dedupe_inplace([0,0,1,1,1,2,2,3,3,4,5,5,5]) == [0,1,2,3,4,5])

# merge test cases
assert(merge_inplace([0], 0, [1], 1) == [1])
assert(merge_inplace([1], 1, [], 0) == [1])
assert(merge_inplace([1,2,3,0,0,0], 3, [2,5,6], 3) == [1,2,2,3,5,6])
assert(merge_inplace([1,4,5,7,9,0,0,0], 5, [1,2,3], 3) == [1,1,2,3,4,5,7,9])
assert(merge_inplace([4,0,0,0], 1, [1,2,3], 3) == [1,2,3,4])
assert(merge_inplace([4,0,0,0], 1, [1,4,6], 3) == [1,4,4,6])
