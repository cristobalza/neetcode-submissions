class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(NxM) space
        # O(NxM) time
        ROWS, COLS = len(matrix), len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    for _r in range(ROWS):
                        matrix[_r][c] = float("-inf")
                    
                    for _c in range(COLS):
                        matrix[r][_c] = float("-inf")
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == float("-inf"): 
                    matrix[r][c] = 0
            