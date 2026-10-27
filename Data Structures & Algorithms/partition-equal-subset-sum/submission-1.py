class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = 0
        for i in nums:
            n += i
        
        if n % 2 != 0 :
            return False
        
        dp = [False] * ((n//2) + 1)
        dp[0] = True

        for i in nums:
            for j in range((n//2),-1,-1):
                if dp[j - i] and j >= i:
                    dp[j] = True
        

        return dp[n//2]

        