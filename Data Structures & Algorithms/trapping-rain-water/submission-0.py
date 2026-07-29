class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0]*len(height)
        rightmax = [0]*len(height)

        for i in range(1,len(leftmax)-1):
            leftmax[i] = max(height[i-1],leftmax[i-1])
        
        for i in range(len(rightmax)-2,0,-1):
            rightmax[i] = max(height[i+1],rightmax[i+1])
        
        units = 0
        for i in range(len(height)):
            temp = min(leftmax[i],rightmax[i]) - height[i]
            if(temp > 0):
                units += temp


        return units
            


        
        