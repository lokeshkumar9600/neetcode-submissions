class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i,cur,val):
            if val == target:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or val > target :
                return
            
            cur.append(nums[i])
            dfs(i,cur,val + nums[i])
            cur.pop()
            dfs(i + 1,cur,val)
        

        dfs(0,[],0)
        return res
        