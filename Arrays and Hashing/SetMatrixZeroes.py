class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows=set()
        columns=set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]==0:
                    rows.add(row)
                    columns.add(col)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in rows or col in columns:
                    matrix[row][col]=0


# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.