class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)

        while(l <= r):
            mid  = (l + r) // 2
            hours_to_eat = 0
            for pile in piles:
                hours_to_eat  = hours_to_eat + math.ceil(pile/mid)

            if hours_to_eat > h:
                l = mid + 1
            elif hours_to_eat <= h:
                r = mid - 1
        
        return l


        