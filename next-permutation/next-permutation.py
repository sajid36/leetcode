class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 0
        length = len(nums)
        for i in range (length-1,0,-1):
            print(nums[i-1], nums[i])
            if nums[i-1] < nums[i]:
                pivot = i
                break
        if pivot == 0:
            nums.sort()
            return
        print(nums[pivot-1])
        swap = length - 1
        while nums[pivot-1] >= nums[swap]:
            print("here")
            print(nums[pivot-1], nums[swap])
            swap -=1
        print(nums[pivot])
        print(swap)
        nums[swap], nums[pivot-1] = nums[pivot-1], nums[swap]
        print(nums)
        
        nums[pivot:] = reversed(nums[pivot:])