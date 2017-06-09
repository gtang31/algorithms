"""
Write a method that finds all the subsets of a set. For example, for the sets S:
S = {a}, the possible subsets of S are [{}, {a}]
S = {a, b}, the possible subsets of S are [{}, {a}, {b}, {a,b}]
S = {a, b, c}, the possible subsets of S are [{}, {a}, {b}, {c}, {a,b}, {a,c},
{b,c}, {a,b,c}]
"""
__author__ = 'Gary Tang'


def power_set(S):
    """
    This problem can be easily solved once we figure out to solve the base
    cases. We just can memoization to save the N-1th subset to solve the Nth by
    iteratively adding a new element to the N-1 subset to create the Nth subset.
    We also need to be careful when updating mutable objects so as to not
    overwrite the previous copies.
    @param S: set
    @return memo: list of sets
    """
    memo = []  # list of subsets

    def recurse(S):
        if not S:
            memo.append(set())
        else:
            ele = S.pop()
            recurse(S)
            copy = list(memo)
            for idx, ss in enumerate(copy):
                copy[idx] = set(ss)
                copy[idx].update(ele)
            memo.extend(copy)
    recurse(S)
    return memo


# test cases
assert(power_set({'a'}) == [set(), {'a'}])
assert(power_set({'a', 'b'}) == [set(), {'b'}, {'a'}, {'a', 'b'}])
assert(power_set({'a', 'b', 'c'}) == [set(), {'b'}, {'c'}, {'b', 'c'}, {'a'}, {'a', 'b'}, {'a', 'c'}, {'a', 'b', 'c'}])
