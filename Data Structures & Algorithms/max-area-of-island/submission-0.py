class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        res = -1

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, visited, area):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            for _r, _c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                area += dfs(_r, _c, visited, area) 

            return area + 1
        
        visited = set() 

        for r in range(ROWS): 
            for c in range(COLS):
                if (r, c) not in visited:
                    res = max(res, dfs(r, c, visited, 0))

        return res

                
        