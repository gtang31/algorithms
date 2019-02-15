"""

"""
import pdb


def word_break(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    wordDict = set(wordDict)
    return _recurse(s, wordDict, set())

def _recurse(string, wordDict, seen):
    print(string)
    pdb.set_trace()
    if (not string) or (string in wordDict):
        # base case
        return True

    substring = ''
    for idx, char in enumerate(string):
        substring += char
        if (substring in wordDict) and (substring not in seen):
            seen.add(substring)
            print("begin recurse")
            if _recurse(string[idx+1:], wordDict, seen):
                return True
    return False


# test cases
# s = "leetcode"
# word_dict = ["leet", "code"]
# assert(word_break(s, word_dict) is True)
s = "aaaaaa"
word_dict = ["aa", "a"]
assert(word_break(s, word_dict) is True)
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# word_dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# assert(word_break(s, word_dict) is False)
# s = "goalspecial"
# word_dict = ["go", "goal", "goals", "special"]
# assert(word_break(s, word_dict) is True)
