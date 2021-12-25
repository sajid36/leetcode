class MyHashMap:

    def __init__(self):
        self.hashMap = {}
        

    def put(self, key: int, value: int) -> None:
        self.hashMap[key] = value
        #print(self.hashMap)

    def get(self, key: int) -> int:
        #print(key)
        #print(self.hashMap)
        if key not in self.hashMap.keys():
            return -1
        else:
            return (self.hashMap[key])

    def remove(self, key: int) -> None:
        if key in self.hashMap.keys():
            del self.hashMap[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)