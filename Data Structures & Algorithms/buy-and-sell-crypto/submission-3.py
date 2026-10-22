class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = float('inf')
        for i in prices:
            minprice = min(minprice, i)
            diff = i - minprice
            profit = max(profit, diff)
        return profit
        


        