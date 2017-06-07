"""
A child is running up a staircase with N steps and can hop either 1, 2, or 3
steps at a time. Calculate all the step permutations the child can run up the
stairs

python -mtimeit -s'from triple_steps import ThreeStepSolution' 'ThreeStepSolution().recursive(30)'
python -mtimeit -s'from triple_steps import ThreeStepSolution' 'ThreeStepSolution().top_down(30)'
"""
__author__ = 'Gary Tang'


class ThreeStepSolution(object):

    def recursive(self, N):
        """
        We solve this problem using recursion.
        """
        if N == 0:
            return 1
        elif N < 0:
            return 0
        else:
            return self.recursive(N-1) + self.recursive(N-2) + self.recursive(N-3)

    def top_down(self, N):
        cache = {0: 1}

        def recurse(N):
            if N < 0:
                return 0
            elif N not in cache:
                cache[N] = recurse(N-1) + recurse(N-2) + recurse(N-3)
            return cache[N]
        return recurse(N)
