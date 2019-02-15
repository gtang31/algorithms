"""
Given a string,  fuind the longest substring containing no
duplicate letters
"""
__author__ = "Gary Tang"


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    longest = 0
    start = 0  # starting index of the sliding window
    seen = {}  # track each character at their last seen index
    for idx, char in enumerate(s):

        if (char in seen) and (seen[char] >= start):
            # condition 1.) we have seen current letter before
            # condition 2.) the letter we saw is also within our sliding window, so don't count it
            # move start index of sliding window to right
            # of last-seen duplicate letter by 1
            start = seen[char]+1
        else:
            # keep iterating through the string keep track
            # of current longest substring
            longest = max(longest, idx-start+1)
        seen[char] = idx
    return longest


ss = ["bdiasbdiqebe"
    , "abcabcbb"
    , "bbbbbb"
    , "bdiasbdiqebewbjha"
    , ""
    , "qw"
    , "wwb"
    , "tmmzuxt"]

for s in ss:
    print(lengthOfLongestSubstring(s))




