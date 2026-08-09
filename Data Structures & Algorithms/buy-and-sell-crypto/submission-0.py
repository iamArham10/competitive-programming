class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[buy]
            if profit >= 0:
                max_profit = max(max_profit, profit)
            
            else:
                buy = i
        
        return max_result


        