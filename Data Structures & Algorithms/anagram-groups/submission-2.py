class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapi = {}
        for i in strs:
            temp = [0]*26
            for j in i:
                temp[ord(j) - ord('a')] += 1
            
            temp_tuple = tuple(temp)
            if temp_tuple in mapi:
                mapi[temp_tuple].append(i)
            else:
                mapi[temp_tuple] = [i]
        
        
        listx = list(mapi.values())
        return(listx)



        