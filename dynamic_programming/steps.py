"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class DistinctSteps(object):

    def __init__(self):
        """
        input n: int. Number of steps
        rtype: int. Number of distinct ways to reach n steps
        """
        # initialize base cases
        self.memo = {1: 1,
                    2: 2}

    def top_down(self, n):
        """
        Work our way down to base case and, from there, use their solutions
        to get answer for n steps. Base cases are n=1 and n=2 since those are
        the only different steps we can do at once.
        """
        def recurse(n):
            if n not in self.memo:
                self.memo[n] = recurse(n-1) + recurse(n-2)
            return self.memo[n]
        return recurse(n)

print(DistinctSteps().top_down(5))
print(DistinctSteps().top_down(6))
print(DistinctSteps().top_down(7))
