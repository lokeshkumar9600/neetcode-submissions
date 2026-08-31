class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        m1 = {}
        m2 = {}

        for i in s:
            if i not in m1:
                m1[i] = 0
            else:
                m1[i] += 1
        
        for i in t:
            if i not in m2:
                m2[i] = 0
            else:
                m2[i] += 1

        
        return m1 == m2
        

        