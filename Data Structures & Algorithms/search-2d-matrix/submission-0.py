class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        # binary search on rows

        top, bottom = 0, ROWS - 1

        while top <= bottom:
            m = (top + bottom) // 2

            if matrix[m][0] < target:
                top = m + 1

            elif target < matrix[m][-1]:
                bottom = m - 1
            
            else: 
                break


        row_list = matrix[m]

        l, r = 0, COLS - 1

        while l <= r:
            m = (l + r) // 2

            if row_list[m] == target:
                return True

            elif row_list[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return True if row_list[l] == target else False