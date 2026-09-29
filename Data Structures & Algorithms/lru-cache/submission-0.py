class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = collections.OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        self.hmap.move_to_end(key)
        return self.hmap[key]
        

    def put(self, key: int, value: int) -> None:
        self.hmap[key] = value
        self.hmap.move_to_end(key)
        if len(self.hmap) > self.capacity:
            self.hmap.popitem(last=False)
