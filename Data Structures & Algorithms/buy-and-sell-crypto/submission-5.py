class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low  = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if(prices[i] > low):
                max_profit = max(max_profit,prices[i] - low)
            
            if(prices[i] < low):
                low = prices[i]

        
        return max_profit

        