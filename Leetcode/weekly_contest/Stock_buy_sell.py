'''
Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
T ~ O(n)
S ~ O(1)
'''

class Solution:
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


arr = [7,1,5,3,6,4]
print(Solution().stocks_buy_sell(arr))






