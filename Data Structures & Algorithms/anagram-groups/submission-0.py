class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for strings in strs:
            count = [0]*26
            for s in strings:
                count[ord(s) - ord("a")] += 1
            
            counter_tup = tuple(count)
            if counter_tup in dictionary:
                dictionary[counter_tup].append(strings)
            else:
                dictionary[counter_tup] = [strings]
        
        return list(dictionary.values())

        
        