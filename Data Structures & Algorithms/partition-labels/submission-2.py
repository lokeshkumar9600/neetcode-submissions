class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapx = {}
        for i in range(len(s)):
                mapx[s[i]] = i
        ans = []
        
        start = 0
        end = 0
        curr_max = 0
        while end < len(s):
         
            for i in range(start,end + 1):
                curr_max = max(curr_max,mapx[s[i]])
            print("curr_max :" ,curr_max , "end : ", end , "start :" , start)
    

            if end == curr_max:
                ans.append(end - start + 1)
                start = end + 1
            
            end += 1
            

        return ans
        