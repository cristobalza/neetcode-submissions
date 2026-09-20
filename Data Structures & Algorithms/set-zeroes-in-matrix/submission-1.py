class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(N) space
        # O(N) time
        ROWS, COLS = len(matrix), len(matrix[0])

        zero_coordinates_set = set()
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zero_coordinates_set.add((r, c))

        for r, c in zero_coordinates_set:
            
            for _r in range(ROWS):
                matrix[_r][c] = 0

            for _c in range(COLS):
                matrix[r][_c] = 0

        
        