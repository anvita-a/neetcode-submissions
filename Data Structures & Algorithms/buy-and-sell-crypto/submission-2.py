class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = float('inf')
        i = 0
        while i < len(prices):
            minprice = min(minprice, prices[i])
            diff = prices[i] - minprice
            profit = max(profit, diff)
            i += 1
        return profit
        


        