import pdb


def min_window(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    from collections import defaultdict
    count_t = defaultdict(int)
    for i in t:
        # keep count of letters in t
        count_t[i] += 1
    group = []
    left = right = 0
    while right < len(s):
        if s[right] in count_t:
            # encountered a character that is in t. But still missing some other letters
            count_t[s[right]] -= 1

        if not any(filter(lambda x: x > 0, count_t.values())):
            # keep incrementing left pointer to minimize window
            last_seen = right
            while count_t[s[last_seen]] <= 0:
                if s[left] in count_t:
                    # add one, bc we will be removing from s[left:right+1]
                    count_t[s[left]] += 1
                    last_seen = left
                left += 1
            # temp should be the smallest substring created from nested while loop
            group.append(s[left-1:right+1])

        right += 1
    group.sort(key = lambda x: len(x), reverse=True)
    return "" if not group else group.pop()


# test cases
S = "ADOBECODEBANC"
T = "ABC"
assert(min_window(S, T) == "BANC")

S = "ADOBECODEBANC"
T = "ABBC"
assert(min_window(S, T) == "BECODEBA")

S = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
T = "A"
assert(min_window(S, T) == "A")
