class CountSquares:

    def __init__(self):
        self.hmap = defaultdict(int) # tuple of points: count
        self.pts = []
        
        

    def add(self, point: List[int]) -> None:
        self.hmap[tuple(point)] += 1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        diag_x, diag_y = point

        for x, y in self.pts:
            if abs(diag_x - x) == abs(diag_y - y) and diag_x != x and diag_y != y:
                res += self.hmap.get((x, diag_y), 0) * self.hmap.get((diag_x, y), 0)

        return res
        
