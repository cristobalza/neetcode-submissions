class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows_hmap = collections.defaultdict(set)
        cols_hmap = collections.defaultdict(set)
        square_hmap = collections.defaultdict(set) # 3x3 

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]

                if val == ".":
                    continue

                elif val in rows_hmap[r] or val in cols_hmap[c] or val in square_hmap[(r//3, c//3)]:
                    return False
                
                else:
                    rows_hmap[r].add(val)
                    cols_hmap[c].add(val)
                    square_hmap[(r//3, c//3)].add(val)

        return True

        