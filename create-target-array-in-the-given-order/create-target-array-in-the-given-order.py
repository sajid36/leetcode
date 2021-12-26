class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        out = []
        for x in range (len(nums)):
            out.insert(index[x], nums[x])
        return out