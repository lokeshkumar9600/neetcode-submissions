class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashi = {}
        for i in range(len(nums)):
            if target - nums[i] in hashi:
                return [hashi[target-nums[i]],i]
            else:
                hashi[nums[i]] = i  

              
        