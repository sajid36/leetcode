class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        x = len(nums)
        res = []
        for i in range (x):
            res.append(nums[nums[i]])
        return res
        