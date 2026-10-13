class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n:
                if grid[r][c] is True:
                    return 1
                return dfs(r + 1, c) + dfs(r, c + 1)

            else:
                return 0


        grid = [[False for _ in range(n)] for _ in range(m)]

        grid[-1][-1] = True


        return dfs(0, 0)
