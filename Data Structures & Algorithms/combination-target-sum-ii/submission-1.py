class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates.sort()
        def dp(i,combi,sumx):

            if sumx == target:
                res.append(combi.copy())
                return
            
            if sumx > target or i >= len(candidates):
                return
                
            
            combi.append(candidates[i])
            
            dp(i + 1,combi,sumx + candidates[i])
            combi.pop()
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
                
            dp(j,combi,sumx)

        dp(0,[],0)
        return res

        