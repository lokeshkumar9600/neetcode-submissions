class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            one = nums[i]
            two = i + 1
            three = len(nums) - 1

            while (two < three):
                if (-one == (nums[two] + nums[three])) :
                    final.append([one,nums[two],nums[three]])
                    
                    two += 1
                    three -= 1

                    while two < three and nums[two] == nums[two - 1]:
                        two += 1

                    while two < three and nums[three] == nums[three + 1]:
                        three -= 1

                elif((nums[two] + nums[three]) > -one):
                    three = three - 1
                elif((nums[two] + nums[three]) < -one):
                    two = two + 1
                
                
        

        return final 






