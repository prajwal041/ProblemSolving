'''
Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
T ~ O(n)
S ~ O(1)
'''
import time
def get_runtime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        runtime = stop - start
        print(f"Total runtime of {func.__name__} is {runtime}")
        return result
    return wrapper

class Solution:
    @get_runtime
    def stocks_buy_sell(self, arr):
        l, r = 0, 1
        max_profit = 0
        n = len(arr)
        while r < n:
            if arr[l] > arr[r]:
                l = r
                r += 1
            else:
                profit = arr[r] - arr[l]
                if max_profit < profit:
                    max_profit = profit
                r += 1

        return max_profit

    @get_runtime
    def maxProfit(self, arr):
        buy, profit = arr[0], 0
        for item in arr[1:]:
            if buy > item:
                buy = item
            profit = max(profit, item - buy)
        return profit

arr = [7,1,5,3,6,4]
s = Solution()
print(f"Output of stocks_buy_sell: {s.stocks_buy_sell(arr)}")
print(f"Output of maxProfit: {s.maxProfit(arr)}")






