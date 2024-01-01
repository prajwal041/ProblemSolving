def maxProfit(prices):
    """
    :param prices:
    :return: maxProfit
    Time : O(n)
    Space : O(1)
    """
    l, r = 0, 1
    maxProfit = 0
    while r < len(prices):
        if prices[l] > prices[r]:
            l = r
        else:
            maxProfit = max(maxProfit, prices[r] - prices[l])
        r += 1
    return maxProfit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
