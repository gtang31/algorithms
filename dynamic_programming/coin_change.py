"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1
"""
import pdb


def coin_change(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    combination = []
    current_sum = amount
    idx = 0
    coins = sorted(coins, reverse=1)
    while idx < len(coins):
        if coins[idx] > current_sum:
            idx += 1
        else:
            combination.append(coins[idx])
            current_sum -= coins[idx]

    print(combination)
    return -1 if not combination or sum(combination) != amount else len(combination)


# test cases
assert(coin_change([1,2,5], 11) == 3)
assert(coin_change([2], 3) == -1)

#figure this out
assert(coin_change([2, 3, 5], 9) == 3)
