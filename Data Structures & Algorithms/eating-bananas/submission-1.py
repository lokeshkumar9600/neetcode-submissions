class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        min_k = right

        while left <= right:
            
            k = (left + right)//2
            temp_h = 0
            for i in piles:
                temp_h += math.ceil(i/k)
            
            if temp_h <= h:
                min_k = min(k,min_k)
                right = k - 1
            else:
                left = k + 1
        
        return min_k

