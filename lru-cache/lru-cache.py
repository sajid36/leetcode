class LRUCache:

    def __init__(self, capacity: int):
        self.res = collections.OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        check = self.res.get(key, None)
        if check is not None:
            self.res.move_to_end(key)
            return check
        else: return -1

    def put(self, key: int, value: int) -> None:
        check = self.res.get(key, None)
        if check:
            self.res.move_to_end(key)
        self.res[key] = value
        
        if len(self.res) > self.cap:
            self.res.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)