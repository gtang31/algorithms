import pdb


class combination_sum():

    def __init__(self):
        self.combinations = []

    def get(self, nums, target):
        """
        find all unique combinations in `nums` that
        sums to `target`
        @param nums: list[int]. List of available numbers to choose from
        @param target: int.
        """
        self._backtrack(sorted(nums), target, [])  # important to sort
        return self.combinations

    def _backtrack(self, nums, target, combination):
        # print('nums: ', nums, ' target:', target, ' combination: ', combination)
        # pdb.set_trace()
        if target == 0:
            # current combination matches target
            combination.sort()
            if combination not in self.combinations:
                self.combinations.append(combination)
            return

        if not nums:
            return

        for idx in range(len(nums)-1, -1, -1):
            if  nums[idx] > target:
                # skip element if it is greater
                # than `target`, it cannot be part of combination
                continue
            self._backtrack(nums[:idx+1], target-nums[idx], combination+[nums[idx]])


# test cases
print(combination_sum().get([2, 3, 6, 7], 7))
print(combination_sum().get([2, 3, 5], 8))
