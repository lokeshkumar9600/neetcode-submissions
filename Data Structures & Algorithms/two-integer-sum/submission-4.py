class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashs = {}
        for index,i in enumerate(nums) :
            if target - i in hashs:
                return [hashs[target-i],index]
            else:
                hashs[i] = index 
        
        return [-1,-1]
        