def maxProfit(prices):
    """
    Description:
        Say you have an array prices for which the ith element is the price of a given stock on day i.
        Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
        Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
    Idea:
        A: peak / valley finding
        B: accumulate the difference
    Complexity:
        Time: O(n)
        Space: O(1)
    """

    # if len(prices) < 2:
    #     return 0
    # total = 0
    # buying = True
    # bought_at = None
    # i = 0
    # while i < len(prices) - 1:
    #     if prices[i] < prices[i+1] and buying:
    #         bought_at = prices[i]
    #         buying = False
    #     if prices[i] > prices[i+1] and not buying:
    #         total += prices[i] - bought_at
    #         buying = True
    #     i += 1
    # if not buying:
    #     total += prices[-1] - bought_at
    # return total

    i = 1
    total = 0
    while i < len(prices):
        if prices[i] > prices[i - 1]:
            total += prices[i] - prices[i - 1]
        i += 1
    return total
