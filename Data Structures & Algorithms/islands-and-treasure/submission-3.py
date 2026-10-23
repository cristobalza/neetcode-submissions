class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        # Enqueue all treasure chests as sources
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):   # process one full layer
                r, c = q.popleft()
                grid[r][c] = dist

                for nr, nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                    if (0 <= nr < ROWS and 0 <= nc < COLS
                            and (nr, nc) not in visited
                            and grid[nr][nc] != -1):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            dist += 1