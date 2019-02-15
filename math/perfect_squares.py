from math import ceil, floor
import pdb


def num_squares(num):
    """
    :type n: int
    :rtype: int
    """
    ops = 0
    for i in range(int(ceil(num**.5)), -1, -1):
        # print(i)
        if i**2 > n:
            continue
        elif i**2 <= n:
            print('{}-{}'.format(num, i**2))
            pdb.set_trace()
            ops += floor(num/(i**2))
            num -= ops*(i**2)

        if num == 0:
            print(int(ops))


n = 12
num_squares(n)
