class Solution:
    def canJump(self, nums: List[int]) -> bool:
        further_distance = 0
        for i in range(len(nums)):

            if i > further_distance:
                return False

            further_distance = max(further_distance, i + nums[i])
        


        return True



            

        