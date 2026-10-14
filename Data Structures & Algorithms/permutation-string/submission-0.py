from collections import Counter
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_seq = Counter(s1)
        window_counter = Counter(s2[:len(s1)])
        if(s1_seq == window_counter):
            return True
        
        for i in range(0,len(s2)-len(s1)):
           window_counter[s2[i]] -= 1
           window_counter[s2[i + len(s1)]] += 1
           if(window_counter == s1_seq):
            return True
        

        return False

        
        