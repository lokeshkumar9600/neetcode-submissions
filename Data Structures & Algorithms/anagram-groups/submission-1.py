class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for s in strs:
            temp = [0] * 26
            for c in s:
                temp[ord(c) - ord('a')] += 1
            
            key = tuple(temp)
            if key in h:
                h[key].append(s)
            else:
                h[key] = [s]
        
        return list(h.values())
        