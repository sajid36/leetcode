class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        out.append(nums[0])
        for x in range (1, len(nums)):
            new = nums[x]
            for y in range (x):
                new = new + nums[y] 
            out.append(new)
        return out