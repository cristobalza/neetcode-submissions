class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])

        area = m * n

        left, right, top, bottom = 0, n, 0, m

        res = []

        while area > 0:

            # to the right
            for c in range(left, right):
                if area <= 0:
                    break
                res.append(matrix[top][c])
                area -= 1

            top += 1

            # to the bottom
            for r in range(top, bottom):
                if area <= 0:
                    break
                res.append(matrix[r][right-1])
                area -= 1

            right -= 1

            # to the right
            for c in range(right - 1, left - 1, -1):
                if area <= 0:
                    break
                res.append(matrix[bottom - 1][c])
                area -= 1

            bottom -= 1


            # to the top

            for r in range(bottom - 1, top - 1, -1):
                if area <= 0:
                    break
                res.append(matrix[r][left])
                area -= 1

            left += 1

        return res

