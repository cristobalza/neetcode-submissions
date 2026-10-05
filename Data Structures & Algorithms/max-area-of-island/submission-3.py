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
            nonlocal area

            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return False

            visited.add((r, c))

            area += 1

            for _r, _c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                dfs(_r, _c, visited)
                
            return True 
        
        visited = set() 

        for r in range(ROWS): 
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    area = 0
                    dfs(r, c, visited)
                    res = max(res, area)

        return res 

                
        