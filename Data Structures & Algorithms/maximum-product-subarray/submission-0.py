class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        front_max = 1
        rear_max = 1

        curr_max = 1
        for i in range(len(nums)):
            if(nums[i] == 0):
                max_product = max(max_product, 0)
                front_max = 1
                continue
            
            front_max = front_max * nums[i]
            max_product = max(front_max, max_product)
        

        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                max_product = max(max_product, 0)
                rear_max = 1
                continue

            rear_max = rear_max * nums[i]
            max_product = max(rear_max,max_product)
        

        return max_product 
        