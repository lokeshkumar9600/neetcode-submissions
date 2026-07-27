class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixproduct = []
        product = 1
        for i in range(len(nums)):
            prefixproduct.append(product)
            product = product*nums[i]
            
            
        
        print(prefixproduct)
        product = 1
        for i in range(len(prefixproduct)-1,-1,-1):
            prefixproduct[i] *= product 
            product *= nums[i]
               

        return prefixproduct        




        
        