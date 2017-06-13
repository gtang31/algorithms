"""
Say you have an array for which the ith element is the price of a given stock
on day i.
If you were only permitted to complete at most one transaction (ie, buy one and
sell one share of the stock), design an algorithm to find the maximum profit.
"""
__author__ = 'Gary Tang'


def max_profit(prices):
    """
    @param prices: list of integers
    @return profit: int representing the maximum profit
    """
    if len(prices) <= 1:
        return 0
    buy_price = prices[0]
    sell_price = prices[1]
    profit = sell_price - buy_price
    for idx in xrange(1, len(prices)-1):
        # update sell price since we cannot sell stocks from a previous date
        sell_price = prices[idx+1]
        if prices[idx] < buy_price:
            # buy low.
            buy_price = prices[idx]
        if sell_price - buy_price > profit:
            # sell high.
            profit = sell_price - buy_price

    if profit < 0:
        return 0
    return profit
