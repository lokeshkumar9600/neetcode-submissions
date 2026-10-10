class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =  []
        result = [0] * len(temperatures)
        for index,temps in enumerate(temperatures):
            if stack:
                while stack and temps > stack[-1][0]:
                        temp = stack.pop()
                        result[temp[1]] = index - temp[1]
                    
            
            stack.append((temps,index))
            
                    

        return result
        