"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Ex:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
__author__ = 'Gary Tang'


class phone_digits:
    def letter_combinations(self, digits):
        """
        Backtracking problem. Think of this as searching a tree
        using DFS
        :type digits: str
        :rtype: List[str]
        """
        output = []
        if not digits:
            return output
        mapping = {'2': 'abc',
                  '3': 'def',
                  '4': 'ghi',
                  '5': 'jkl',
                  '6': 'mno',
                  '7': 'pqrs',
                  '8': 'tuv',
                  '9': 'wxyz'}
        def backtrack(nums, s):
            """help function for DFS"""
            if not nums:
                output.append(s)
                return
            for char in mapping.get(nums[0]):
                backtrack(nums[1:], s+char)
        backtrack(digits, '')
        return output


print(phone_digits().letter_combinations("5845"))
print(phone_digits().letter_combinations("23"))