class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        comp1 = [0] * 26
        comp2 = [0]* 26
        for c in s:
            comp1[ord(c) - ord('a')] += 1
        
        for c in t:
            comp2[ord(c) - ord('a')] += 1

        return comp1 == comp2

        
        

        