class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        l = 0
        r = 0
        size = 0
        while r < len(s):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            r += 1
            size = max(size,r-l)
    
        return size


            

        