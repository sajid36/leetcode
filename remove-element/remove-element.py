class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for i in range (len(nums)):
            if nums[i]!=val:
                nums[counter] = nums[i]
                counter = counter + 1
            else:
                continue
        return (counter)