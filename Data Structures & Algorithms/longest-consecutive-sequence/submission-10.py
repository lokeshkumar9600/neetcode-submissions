class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        setx = set(nums)
        lenx = 0

        for i in range(len(nums)):
            if nums[i] -1 not in setx:
                start = nums[i]
                count = 0
                while start in setx:
                    setx.remove(start)
                    count += 1
                    start += 1

                
                lenx = max(lenx,count)
                

        return lenx

        
        