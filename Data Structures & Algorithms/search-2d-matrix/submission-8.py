class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        row = len(matrix)
        cols = len(matrix[0])
        right = row * cols - 1

        while (left <= right):
            mid = (left + right) // 2
            r = (mid) // cols
            c = (mid) % cols

            if(matrix[r][c] == target):
                return True
            
            if(target > matrix[r][c]):
                left = mid + 1
            
            if(target < matrix[r][c]):
                right = mid - 1
        

        return False
        