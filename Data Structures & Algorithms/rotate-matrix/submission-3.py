class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Given matrix

        R: none, but inplace rotate the matrix input into 90 degree clockwise

        Transpose 

        matrix = [
            [1,2],
            [3,4]
        ]

        => 
        matrix = [
            [1, 3],
            [2, 4]
        ]

        for r in range(ROWS)
            for c in range(r, COLS)
                matrix[r][c] matrix[c][r]

        Reflection y axis 

        matrix = [
            [3, 1],
            [4, 2]
        ]

        swap the values for the columns

        for c in range(cols // 2)
            matrix[c] matrix[COlS - 1 - c]


        """

        ROWS, COLS = len(matrix), len(matrix[0])

        # Transpose
        for r in range(ROWS):
            for c in range(r, COLS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Reflection y axis
        for row in matrix:
            for c in range(COLS // 2):
                row[c], row[COLS - 1 - c] = row[COLS - 1 - c], row[c]

        