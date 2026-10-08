class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for strings in strs:
            temp = [0] * 26
            for s in strings:
                temp[ord(s) - ord('a')] += 1
            
            comp_set = tuple(temp)
            if comp_set in results:
                results[comp_set].append(strings)
            else:
                results[comp_set] = [strings]
        
        return list(results.values())
        
            


        