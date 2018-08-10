"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Ex:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
__author__ = 'Gary Tang'


class phone_digits:
    """
    Think of this as a DFS problem traversing a K-ary tree. Keep building out the combinations until we reach a "leaf".
    """
    def __init__(self):
        self.map = {'2': 'abc'
                   , '3': 'def'
                   , '4': 'ghi'
                   , '5': 'jkl'
                   , '6': 'mno'
                   , '7': 'pqrs'
                   , '8': 'tuv'
                   , '9': 'wxyz'}
        self.output = []

    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return self.output

        self._recurse('', digits)
        return self.output

    def _recurse(self, current_combo, remaining_digits):
        """
        DFS helper function
        """
        if not remaining_digits:
            self.output.append(current_combo)
            return

        current_digit = remaining_digits[0]
        for char in self.map[current_digit]:
            self._recurse(current_combo+char, remaining_digits[1:])


# test cases
print(phone_digits().letter_combinations("5845"))
assert(phone_digits().letter_combinations("9") == ['w', 'x', 'y', 'z'])
assert(phone_digits().letter_combinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"])

