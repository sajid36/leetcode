class Solution:
    def binarySearch(self, nums, target,left, right, res):
        if left > right:
            return False
        mid = (left + right)//2
        if nums[mid]== target:
            res[0] = mid
            return
        else:
            if nums[mid] > target:
                self.binarySearch(nums,target,left, mid-1, res)
            else:
                self.binarySearch(nums,target,mid+1, right, res)
                
    def search(self, nums: List[int], target: int) -> int:
        minimum  = min(nums)
        idx = nums.index(minimum)
        result = -1
        n = len(nums)
        if idx != 0:
            if target>=nums[0]:
                nums = nums[:idx]
            else:
                nums = nums[idx:n]
                result = idx
        n = len(nums)
        left = 0
        right = n-1
        res = [-2]*1
        self.binarySearch(nums, target, left, right, res)
        if res[0]==-2:
            return -1
        else:
            if result== -1:
                return res[0]
            else:
                return res[0]+result
        
        