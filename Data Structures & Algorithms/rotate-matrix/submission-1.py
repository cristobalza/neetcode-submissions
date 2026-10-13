class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        """

        matrix=[
            [1,2],
            [3,4]
            
        ]

        Transpose:

        matrix=[
            [1, 3],
            [2, 4]
        ]

        Reflection on cols:

        matrix=[

            [3, 1],
            [4, 2]
        ]



        """
        
        ROWS, COLS = len(matrix), len(matrix[0])

        # Transpose

        for r in range(ROWS):
            for c in range(r, COLS):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Reflection on cols

        for r in range(ROWS):
            # matrix[r].reverse()
            for c in range(COLS // 2):
                matrix[r][c], matrix[r][COLS - 1 - c] = matrix[r][COLS - 1 - c], matrix[r][c]


        