import heapq
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        freq_map = collections.Counter(nums)

        for elem,count in freq_map.items():
            freq[count].append(elem)
        
        result = []
        for i in range(len(freq) - 1 ,0,-1):
            for y in freq[i]:
                if len(result) < k :
                    result.append(y)
        

        return result



        


        

        


        