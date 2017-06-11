"""
Construct fibonacci square. To see the different O(n) time complexity for each
implemtation, run script as (including single quotes):

python -mtimeit -s'from dynamic_programming.fibonacci import FibonacciSolution' 'FibonacciSolution().recursive(30)'
python -mtimeit -s'from dynamic_programming.fibonacci import FibonacciSolution' 'FibonacciSolution().top_down(100)'
python -mtimeit -s'from dynamic_programming.fibonacci import FibonacciSolution' 'FibonacciSolution().bottom_up(100)'
"""
__author__ = 'Gary Tang'


class FibonacciSolution(object):
    """
    a series of numbers in which each number ( Fibonacci number ) is the sum of
    the two preceding numbers
    """

    def recursive(self, n):
        """
        recursively create fibonacci square. Runs in O(2^n) time where is the
        number of recursive calls. This is due to the naive recursion process
        having to re-calculate each fibonacci seqeuences for each number
        """
        if (n == 0) or (n == 1):
            return n
        elif n < 0:
            raise ValueError('No sequence can be created starting from {}'.format(n))
        return self.recursive(n-1) + self.recursive(n-2)

    def top_down(self, n):
        """
        uses memoization to cache the fibonacci number to avoid having to
        re-calculate them for every new n. O(n)
        """
        cache = {}

        def recurse(n):
            """Helper function. Populate cache with fibonacci numbers"""
            if (n == 0) or (n == 1):
                # base case
                cache[n] = n
            if n not in cache:
                cache[n] = recurse(n-1) + recurse(n-2)
            return cache[n]
        return recurse(n)

    def bottom_up(self, n):
        """
        same as top-down approach, but reversed. We build the solution starting
        from the base case and work our way up
        """
        n_0, n_1 = 1, 1
        for i in xrange(2, n):
            result = n_0 + n_1
            n_0, n_1 = n_1, result
        return n_1
