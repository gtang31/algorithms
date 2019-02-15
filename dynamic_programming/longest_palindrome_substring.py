"""
Find the longest
"""


def longest_palindrome_substring(string):

    longest = ''
    # expand around center approach
    for idx in range(len(string)):
        # pdb.set_trace()
        odd_len = expand(string, idx, idx)  # N potential odd-length palindrome centers
        even_len = expand(string, idx, idx+1)  # N-1 potential even-length palindrome centers
        longest = max([longest, odd_len, even_len], key=lambda x: len(x))
    return longest

def expand(s, left, right):
    # gradually increment left/right indices of `s` and check whether it is still a palindrome
    palindrome = ''
    while (left >= 0) and (right < len(s)):
        if s[left] == s[right]:
            palindrome = s[left:right+1]
            left -= 1
            right += 1
        else:
            break
    return palindrome


# test case
print(longest_palindrome_substring("a"))
print(longest_palindrome_substring("babad"))
print(longest_palindrome_substring("cbbd"))
print(longest_palindrome_substring("cbfdsaoindsawracecarbd"))
print(longest_palindrome_substring(""))
print(longest_palindrome_substring("dbracecarwasdnioasdfbc"))
print(longest_palindrome_substring("racecar"))
print(longest_palindrome_substring("cb"))
