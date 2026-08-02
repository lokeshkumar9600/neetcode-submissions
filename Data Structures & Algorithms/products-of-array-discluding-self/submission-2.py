class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix_sum = 1
        for i in range(len(nums)):
            prefix.append(prefix_sum)
            prefix_sum = nums[i] * prefix_sum
        
        
        postfix = 1
        for i in range(len(prefix)-1,-1,-1):
            prefix[i] *= postfix
            postfix *= nums[i]


        return prefix
        