class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dfs(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            
            elif r >= m or c >= n:
                return 0
            
            elif (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)

            return memo[(r, c)]

        memo = {}
        return dfs(0, 0)
