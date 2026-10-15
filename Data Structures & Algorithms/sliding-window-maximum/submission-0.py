class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        current_max = max(nums[:k])
        ans = []
        ans.append(current_max)

        for i in range(0,len(nums) - k):
            if nums[(i + k)] > current_max:
                current_max = nums[(i +k)]
                
            
            if nums[i] == current_max:
                temp_max = max(nums[i + 1:i + k + 1])
                current_max = temp_max
            
            ans.append(current_max)
        
        

        return ans


        