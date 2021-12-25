class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 1: return 
        counter = 1
        last = nums[0]
        for i in range (1, len(nums)):
            if nums[i]!=last:
                nums[counter] = nums[i]
                counter = counter + 1
                last = nums[i]
            else:
                continue

        return (counter)