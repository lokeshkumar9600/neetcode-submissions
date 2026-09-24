class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashi = {}
        for i in nums:
            if i in hashi.keys():
                return True
            else:
                hashi[i] = 1
        

        return False


        