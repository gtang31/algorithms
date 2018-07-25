"""
Write a method that finds all the subsets of a set. For example, for the sets S:
S = {a}, the possible subsets of S are [{}, {a}]
S = {a, b}, the possible subsets of S are [{}, {a}, {b}, {a,b}]
S = {a, b, c}, the possible subsets of S are [{}, {a}, {b}, {c}, {a,b}, {a,c},
{b,c}, {a,b,c}]
"""
import pdb
__author__ = 'Gary Tang'


def power_set(S):
    """
    This problem can be easily solved once we figure out to solve the base
    cases. We just can memoization to save the N-1th subset to solve the Nth by
    iteratively adding a new element to the N-1 subset to create the Nth subset.
    We also need to be careful when updating mutable objects so as to not
    overwrite the previous copies.
    @param S: set
    @return memo: list of lists
    """
    memo = []  # list of lists

    def recurse(S):
        if not S:
            memo.append(list())
        else:
            ele = S.pop()
            recurse(S)
            # pdb.set_trace()
            copy = memo[:]
            for i, ss in enumerate(copy):
                # print(i, ss)
                copy[i] = ss[:]  # create NEW copy of i-th element in `copy`
                copy[i].append(ele)  # add letter back
            memo.extend(copy)
    recurse(S)
    print(memo)
    return memo


# test cases
assert(power_set(['a']) == [[], ['a']])
assert(power_set(['a', 'b']) == [[], ['a'], ['b'], ['a','b']])
assert(power_set(['a', 'b', 'c']) == [[], ['a'], ['b'], ['a','b'], ['c'], ['a','c'], ['b','c'], ['a','b','c']])
