"""
Given a list of integers, return a list of all the permutations.
"""


def permute(nums):
    """
    Perform backtracking to find all permutations
    Ex: nums = [1,2,3]
              __R__
             /  |  \
          __1   2   3__
         /\    / \    /\
        2  3  1   3  1  2
    Total of 6 different permutations
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ret = []
    def backtrack(nums, perm):
        # base case
        if not nums:
            ret.append(list(perm))
        else:
            for idx, i in enumerate(nums):
                perm.append(i)
                backtrack(nums[0:idx]+nums[idx+1:], perm)
                perm.pop()
        return

    backtrack(nums, [])
    print(ret)
    return ret


assert(len(permute([1,2,3])) == 6)
