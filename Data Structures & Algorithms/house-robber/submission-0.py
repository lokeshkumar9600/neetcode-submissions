class Solution:
    def rob(self, nums: List[int]) -> int:

        def robhouse(i , dp):
            
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0],nums[1])

            if(dp[i] != -1):
                return dp[i]

            dp[i] = max(robhouse(i - 2,dp) + nums[i] , robhouse(i-1,dp))

            return dp[i]


        dp = [-1] * (len(nums) + 1)
        return robhouse(len(nums)-1,dp)    
        







        