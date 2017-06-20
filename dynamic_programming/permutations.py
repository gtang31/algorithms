"""
Write a method to compute all permutations of a string
"""
__author__ = 'Gary Tang'


class PermutationSolution(object):

    def without_dupes(self, s):
        """
        Create permutations from a string without duplicates. We do a top-down
        approach and build a permutation for N characters by building off the
        solution for N-1 characters. We insert the Nth character into all
        positions for each of the N-1 permutations. This runs in O(n!) time.
        """
        if len(s) == 1:
            return set([s])
        char, r = s[0], set()
        perms = self.without_dupes(s[1:])
        for perm in perms:
            for idx in range(len(perm)+1):
                # insert char into all locations for each permutation
                r.add(perm[0:idx]+char+perm[idx:])
        return r


# test cases
assert(PermutationSolution().without_dupes('ab')) == set(['ab', 'ba'])
assert(PermutationSolution().without_dupes('abc')) == set(['abc', 'cab', 'bac', 'cba', 'acb', 'bca'])
assert(PermutationSolution().without_dupes('abcd')) == set(['abcd', 'abdc', 'acbd', 'acdb', 'adbc', 'adcb', 'bacd', 'badc', 'bcad', 'bcda', 'bdac', 'bdca', 'cabd', 'cadb', 'cbad', 'cbda', 'cdab', 'cdba', 'dabc', 'dacb', 'dbac', 'dbca', 'dcab', 'dcba'])
