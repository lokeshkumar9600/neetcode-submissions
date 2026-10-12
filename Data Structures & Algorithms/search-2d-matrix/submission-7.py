class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in range(len(matrix)):
            left = 0
            right = len(matrix[m]) - 1
            while (left <= right):
                mid = (left + right) // 2
                if(matrix[m][mid] == target):
                    return True
                
                if(target > matrix[m][mid]):
                    left = mid + 1
                
                if(target < matrix[m][mid]):
                    right = mid - 1
        

        return False

        