"""
Input: "A man, a plan, a canal: Panama"
Output: true

Input: "race a car"
Output: false
"""
import re


def is_palindrome(s):
    s = re.sub('\W', '', s.lower())  # remove nonalpha values
    forward = 0
    backward = len(s)-1
    while forward <= backward:
        if s[forward] != s[backward]:
            return False

        forward += 1
        backward -= 1 
    return True


assert(is_palindrome("A man, a plan, a canal: Panama") is True)
assert(is_palindrome("race a car") is False)