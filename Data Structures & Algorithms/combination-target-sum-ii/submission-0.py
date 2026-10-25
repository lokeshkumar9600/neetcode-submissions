class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()


        def dfs(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or i >= len(candidates):
                return

            #include the element at index i
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            var = 0
            cur.pop()
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            
            dfs(j,cur,total)

        
        dfs(0,[],0)
        return res

            


            
        