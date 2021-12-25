class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos1 = 0
        for i in range (len(nums)):
            if nums[i] == 0:
                nums.insert(0,nums[i])
                del nums[i+1]
                pos1 = pos1 + 1
            elif nums[i] == 1:
                nums.insert(pos1,nums[i])
                del nums[i+1]
            
                