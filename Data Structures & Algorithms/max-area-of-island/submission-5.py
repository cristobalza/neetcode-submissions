class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """

        grid=[
        [0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0], [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]



        """
        
        res = 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, visited):

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            local_area = 0
            for _r, _c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                local_area += dfs(_r, _c, visited)
                
            return 1 + local_area
        
        visited = set() 

        for r in range(ROWS): 
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    res = max(res, dfs(r, c, visited))

        return res 

                
        