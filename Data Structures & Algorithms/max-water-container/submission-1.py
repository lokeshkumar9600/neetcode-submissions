class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #a two pointer approach total area = width * height
        # width  = right - left 
        #height = min(heights[right],heights[left])
        left = 0
        right = len(heights)-1
        max_area = 0

        while left < right:
            area = (right - left) * min(heights[right],heights[left]) #right-left gives the width , we take minimum of the two heights cause water will overflow so height of the container will be the min of the two heights
            max_area = max(max_area,area)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_area




        