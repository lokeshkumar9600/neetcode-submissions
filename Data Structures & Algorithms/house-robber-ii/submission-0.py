class Solution:
    def rob(self, nums: List[int]) -> int:


        if len(nums) == 1:
            return nums[0]

        
        def helper(arr):
            dp = [-1] * (len(arr) + 1)

            def go(i):
                if i == 0:
                    return arr[0]
                if i == 1:
                    return max(arr[0], arr[1])
                if dp[i] != -1:
                    return dp[i]
                dp[i] = max(go(i - 2) + arr[i], go(i - 1))
                return dp[i]
        

            return go(len(arr)-1)

        return max(helper(nums[:-1]),helper(nums[1:]))
        