class Solution:

    def __init__(self, nums: List[int]):
        
        self.res = {}
        
        for i in range (len(nums)):
            if nums[i] not in self.res.keys():
                self.res[nums[i]] = list()
                self.res[nums[i]].append(i)
            else:
                self.res[nums[i]].append(i)
                
        

    def pick(self, target: int) -> int:
        targetList = self.res[target]
        ran = random.randint(0,len(targetList)-1)
        return targetList[ran]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)