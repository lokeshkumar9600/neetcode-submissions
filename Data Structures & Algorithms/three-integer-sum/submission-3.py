class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        ans = []
        while(i < len(nums)):
            if(i > 0 and nums[i] == nums[i-1]):
                i += 1
                continue

            nums1 = nums[i]
            left = i + 1
            right = len(nums) - 1
            while(left < right):
                if((nums[left] + nums[right]) == -(nums1)):
                    ans.append([nums1,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1

                 
                elif (nums[left] + nums[right]) > -(nums1):
                    right -= 1
                else:
                    left += 1
            
            i += 1
                

            
            
        
        return ans
        