class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, visited, i):
            if i == len(word):
                return True
            if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited and board[r][c] == word[i]:
                visited.add((r, c))
                for _r, _c in [(r + 1,c), (r - 1,c), (r,c + 1), (r,c - 1)]:
                    if dfs(_r, _c, visited, i + 1):
                        return True
                visited.remove((r, c))

            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, set(), 0):
                        return True

        return False
        