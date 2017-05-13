"""
Given a string, check to see whether it is an anagram of a palindrome. The string
does not need to be a valid english word.
"""
import pdb
from collections import defaultdict
__author__ = "Gary Tang"


class isAnagramPalindromeSolution(object):
    """
    In order for a string to be a palindrome, each character must occur even
    amount of times if the length of the string is even value. If the string is
    odd length long, then only one character can occur odd amount of times. We
    solve this problem in two different ways.
    """
    def __init__(self, s=""):
        self.s = s
        self._s_len = len(s)
        self._odd_occur = False

    def _basic_checks(self):
        pass

    def use_hash(self):
        """
        keep count of each character's occurrence. At most only one character
        may occur odd amount of times.
        """
        # populate dict with character counts
        d = defaultdict(int)
        for char in self.s:
            d[char] += 1

        # check whether at most one character has odd count
        for k in d.keys():
            if d[k] % 2 == 1:
                if self._s_len % 2 == 0:
                    # found odd occurrence in even length s
                    return False

                if not self._odd_occur:
                    # found first odd occurence
                    self._odd_occur = True
                else:
                    # found more than one odd occurence
                    return False
        return True

    def use_bit_vector(self):
        """
        no additional data structures used. Use a bit vector to track whether
        any character occurred odd amount of times. We do not need to actually
        track character counts, only odd or even
        """
        bit_vector = 0  # bit vector of length 26
        for char in self.s:
            mask = ord(char)-ord('a')
            if 1 << mask | bit_vector == bit_vector:
                # flipping a bit 1 -> 0
                bit_vector ^= 1 << mask
            elif 1 << mask | bit_vector > bit_vector:
                # a bit was flipped 0 -> 1. An odd occurence
                bit_vector |= 1 << mask
        ones_count = bin(bit_vector).count('1')
        if (self._s_len % 2 == 0) and (ones_count != 0):
            return False
        elif (self._s_len % 2 == 1) and (ones_count != 1):
            return False
        return True


# Test cases
assert isAnagramPalindromeSolution().use_hash() is True
assert isAnagramPalindromeSolution("tcoatca").use_hash() is True
assert isAnagramPalindromeSolution("plwq").use_hash() is False
assert isAnagramPalindromeSolution("fewwf").use_hash() is True
assert isAnagramPalindromeSolution().use_bit_vector() is True
assert isAnagramPalindromeSolution("tcoatca").use_bit_vector() is True
assert isAnagramPalindromeSolution("plwq").use_bit_vector() is False
assert isAnagramPalindromeSolution("fewwf").use_bit_vector() is True
