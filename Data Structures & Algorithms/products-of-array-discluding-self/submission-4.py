class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        run_sum  = 1
        temp_num = list(nums)
        for i in range(len(nums)):
            run_sum = run_sum * nums[i]
            nums[i] = run_sum
        
        right_sum = 1
        
        for i in range(len(temp_num)-1,-1,-1):
                temp = temp_num[i]
                if i == 0:
                    temp_num[i] = 1*right_sum
                    continue
                    
                temp_num[i] = nums[i-1]*right_sum
                right_sum *= temp
            

        

        return temp_num


        