class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indexes = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    indexes.add((row, col))
        
        for row, col in indexes:
            for row1 in range(len(matrix)):
                matrix[row1][col] = 0
            
            for col1 in range(len(matrix[0])):
                matrix[row][col1] = 0