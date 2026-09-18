class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(r, c, prev_height, visited):
            if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visited and heights[r][c] >= prev_height:
                visited.add((r, c))

                for _r, _c in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    dfs(_r, _c, heights[r][c], visited)

            return 
        

        ROWS, COLS = len(heights), len(heights[0])
        
        pacific_set = set()
        for r in range(0, ROWS):
            dfs(r, 0, heights[r][0], pacific_set)
        for c in range(0, COLS):
            dfs(0, c, heights[0][c], pacific_set)
                

        atlantic_set = set()
        for r in range(ROWS - 1, -1, -1):
            dfs(r, COLS - 1, heights[r][COLS - 1], atlantic_set) 
        for c in range(COLS - 1, -1, -1):
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atlantic_set) 
        
        res = []

        print(pacific_set)
        print(atlantic_set)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific_set and (r, c) in atlantic_set:
                    res.append([r, c])

        return res