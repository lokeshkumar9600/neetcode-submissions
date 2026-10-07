class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for x,y in enumerate(nums):
            if target - y in hashmap:
                return [hashmap[target-y],x]
            else:
                hashmap[y] = x
        