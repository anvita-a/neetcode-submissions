class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for a in range(1, amount+1):
            dp[a] = min((dp[a-c]+1 for c in coins if c<=a), default = float('inf'))
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]
        