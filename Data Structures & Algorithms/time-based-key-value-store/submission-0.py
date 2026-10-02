class TimeMap:

    def __init__(self):
        self.hmap = collections.defaultdict(list) # key: [timestamp, value]
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.hmap[key].append((timestamp, value))
     
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        
        idx = self.search(self.hmap[key], timestamp)

        if idx < 0:
            return ""

        return self.hmap[key][idx][1]

    
    def search(self, lst, time_target):

        l, r = 0 , len(lst) - 1

        while l <= r:
            m = (l + r) // 2
        
            if lst[m][0] < time_target:
                l = m + 1
            elif time_target < lst[m][0]:
                r = m - 1

            else:
                return m

        return r
        

        
