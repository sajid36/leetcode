class Solution:

    def __init__(self, w: List[int]):
        self.w = []
        
        total = 0
        for item in w:
            total = total + item
            self.w.append(total)
            
        self.total = total
        

    def pickIndex(self) -> int:
        ran = random.randint(1, self.total)
        for index, weight in enumerate(self.w):
            if ran <= weight:
                return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()