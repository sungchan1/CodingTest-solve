class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_rows = set()
        zero_cols = set()

        row_length = len(matrix)
        col_length = len(matrix[0])

        for row in range(row_length):
            for col in range(col_length):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for zero_row in zero_rows:
            matrix[zero_row] = [0] * col_length

        for zero_col in zero_cols:
            for row in range(row_length):
                matrix[row][zero_col] = 0 
        


        