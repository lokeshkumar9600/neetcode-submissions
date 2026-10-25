class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def mincost(i,dp):
            if i == 0 or i == 1:
                return cost[i]

            if dp[i] != -1:
                return dp[i]

            dp[i] = cost[i] + min(mincost(i-1,dp),mincost(i-2,dp))
            return dp[i]

        
        n = len(cost)
        dp = [-1] * n
        return min(mincost(n-1,dp),mincost(n-2,dp))


        