from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        t_chars = Counter(t)
        w_chars = Counter()

        need = len(t_chars)
        have = 0

        min_len = float("inf")
        start = 0
        l = 0
        for r in range(len(s)):
            if s[r] in t_chars:
                w_chars[s[r]] += 1
            
                if w_chars[s[r]] == t_chars[s[r]]:
                    have += 1
            
            while have == need:
                window_len = r - l + 1

                if window_len < min_len:
                    min_len = window_len
                    start = l
                
                if s[l] in t_chars:
                    if w_chars[s[l]] == t_chars[s[l]]:
                        have -= 1
                    
                    w_chars[s[l]] -= 1
                
                l += 1
        

        return "" if min_len == float("inf") else s[start: start + min_len]


            







        
        