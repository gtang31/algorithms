"""
Create an algorithm to print all valid combinations of N pairs of parentheses
To test the run time between a recursive vs. memoization approach:

python -mtimeit -s'from dynamic_programming.valid_parentheses import ParenthesesSolution' 'ParenthesesSolution().recursive(13)'
python -mtimeit -s'from dynamic_programming.valid_parentheses import ParenthesesSolution' 'ParenthesesSolution().top_down(13)'

742900 permutations
"""
__author__ = 'Gary Tang'


class ParenthesesSolution(object):

    def __init__(self):
        pass

    def recursive(self, N):
        """
        in this recursive approach, we insert a new pair of parenthesis to the
        N-1 combinations of parentheses. Using this approach, we waste a lot of
        time re-creating duplicates
        @param N: int. Number of valid parentheses to permute
        """
        if N == 1:
            return set(['()'])
        sub_soln = self.recursive(N-1)
        r = set()
        for permutation in sub_soln:
            for idx, paren in enumerate(permutation):
                if paren == '(':
                    # insert `()` after opening parenthesis
                    r.add(permutation[0:idx+1]+'()'+permutation[idx+1:])
            # pre-pend a `()` to a permutation
            r.add('()'+permutation)
        return r

    def top_down(self, N):
        """
        Use combinatorics to add parenthesis by keeping track of opening and
        closing parenthesis
        - Add `(` when the the number of opening parentheses is greater than N
        and recurse. This will create the '(((...' pattern.
        - Add closing parenthesis when the number of opening parenthesis is less
        than the number of closing parenthesis.
        This will complete the valid parentheses pair `)))`
        As we go back up the call stack, this approach will create the alternating
        `()(())` etc.
        @param n: number of parentheses to permute
        @return r: set
        """
        num = N*2
        permutation = [None]*num
        r = set()

        def recurse(left, right):
            if (left == 0) and (right == 0):
                r.add(''.join(permutation))
            idx = num - left - right  # track which index to insert parenthesis
            if left > 0:
                permutation[idx] = '('
                # print('left', left, right, permutation)
                recurse(left-1, right)
            if left < right:
                permutation[idx] = ')'
                # print('right', left, right, permutation)
                recurse(left, right-1)
        recurse(N, N)
        return r
