class Node:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.capacity = capacity

        self.left = Node(-1,-1)
        self.right = Node(-1,-1)

        self.left.next, self.right.prev = self.right, self.left

    def pop(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def move_to_end(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        self.pop(self.hmap[key])
        self.move_to_end(self.hmap[key])
        return self.hmap[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.pop(self.hmap[key])
        self.hmap[key] = Node(key, value)
        self.move_to_end(self.hmap[key])

        # Check cap
        if len(self.hmap) > self.capacity:
            lru = self.left.next
            self.pop(lru)
            del self.hmap[lru.key]


        
