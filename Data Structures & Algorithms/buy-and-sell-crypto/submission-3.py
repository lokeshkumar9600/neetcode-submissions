class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        min_selling = prices[0]
        for i in range(1,len(prices)):
            min_selling = min(min_selling,prices[i])
            maxprofit = max(maxprofit,prices[i] - min_selling)

        

        return maxprofit
        