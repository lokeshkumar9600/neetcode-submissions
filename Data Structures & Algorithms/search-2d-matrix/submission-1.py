class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                left = 0
                right = len(matrix[0]) - 1
                while left <= right:
                    mid = (left + right) //2
                    if(matrix[i][mid] == target):
                        return True
                    elif target > matrix[i][mid]:
                        left = left + 1
                    else:
                        right = right - 1
            
        
        return False

        