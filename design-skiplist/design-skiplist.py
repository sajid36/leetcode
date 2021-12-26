class Skiplist:

    def __init__(self):
        self.res={}
        

    def search(self, target: int) -> bool:
        if target in self.res.keys():
            return True

    def add(self, num: int) -> None:
        if num in self.res.keys():
            self.res[num] = self.res[num] + 1
        else:
            self.res[num] = 1
        

    def erase(self, num: int) -> bool:
        if num in self.res.keys():
            if(self.res[num] == 1):
                del self.res[num]
                return True
            else:
                self.res[num] = self.res[num] - 1
                return True
                
        else:
            return False


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)