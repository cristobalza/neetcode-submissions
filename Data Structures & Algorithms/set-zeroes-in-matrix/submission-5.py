class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(NxM) space
        # O(1) time
        ROWS, COLS = len(matrix), len(matrix[0])

        first_row = any(matrix[0][c] == 0 for c in range(COLS))
        first_col = any(matrix[r][0] == 0 for r in range(ROWS))

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0


        if first_col:
            for r in range(ROWS):
                matrix[r][0] = 0

        if first_row:
            for c in range(COLS):
                matrix[0][c] = 0
