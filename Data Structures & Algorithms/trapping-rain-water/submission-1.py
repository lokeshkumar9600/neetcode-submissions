class Solution:
    def trap(self, height: List[int]) -> int:
        leftmaxi = [0] * len(height)
        rightmaxi = [0] * len(height)
        leftmax = 0
        rightmax = 0
        for i in range(len(height)):
            leftmaxi[i] = leftmax
            leftmax = max(leftmax,height[i])
        
        for i in range(len(height)-1,-1,-1):
            rightmaxi[i] = rightmax
            rightmax = max(rightmax,height[i])

        water_store = 0
        for i in range(len(height)):

            if(min(leftmaxi[i],rightmaxi[i]) - height[i] >= 0):
                water_store += (min(leftmaxi[i],rightmaxi[i]) - height[i])
        

        return water_store


        



        