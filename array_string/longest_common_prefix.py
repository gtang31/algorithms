def find_lcp(strs):
    """
    Iterate the smallest string s. For each string in strs, we compare its
    character at index `idx` to s[idx]. Maximum runtime is O(m*n) where m is
    length of s and n is length of strs.
    :type strs: List[str]
    :rtype: str
    """
    # sort strs by length of each element in descending order
    strs.sort(key=lambda x: len(x), reverse=1)
    shortest = strs.pop()
    current_prefix = ''

    # vertical comparison. Time complexity O(m*n), where m is length of shortest string in strs
    # and n is length of strs
    for idx in range(len(shortest)):
        current_prefix += shortest[idx]
        for string in strs:
            if string[:idx+1] != current_prefix:
                return current_prefix[:idx]
    return current_prefix


assert(find_lcp(["flower","flow","flight"]) == "fl")
assert(find_lcp(["dog","racecar","car"]) == "")
assert(find_lcp(["flower","flowers","flowering","flowered"]) == "flower")

