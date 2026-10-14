class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] in ["X", "S"]:
                return
            
            board[r][c] = "S"

            for _r, _c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                dfs(_r, _c)

            return

        # check edges
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0 or r == ROWS - 1 or c == COLS -1):
                    dfs(r, c)

        # check the rest
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
