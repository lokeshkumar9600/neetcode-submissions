class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_array = [0]*26
        t_array = [0]*26
        for i in s:
            s_array[ord(i) - ord('a')] += 1
        
        for j in t:
            t_array[ord(j) - ord('a')] += 1
        

        return s_array == t_array



        