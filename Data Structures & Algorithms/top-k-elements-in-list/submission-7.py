import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 1
        
        pq = []
        result = []
        for element,frequency in freq_map.items():
            heapq.heappush_max(pq,(frequency,element))
        
        for i in range(k):
            freq,elem = heapq.heappop_max(pq)
            result.append(elem)
        

        return result
        


        

        


        