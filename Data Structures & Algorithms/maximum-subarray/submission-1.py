class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        running_sum = 0

        for i in nums:
            running_sum += i
            maxsum = max(running_sum,maxsum)
            if running_sum < 0:
                running_sum = 0
        

        return maxsum

        