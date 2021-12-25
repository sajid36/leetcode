class Solution:
    def binarySearch(self, nums:List[int], target:int, response:List[int], left: int, right:int):
        
        if left > right:
            return False    
        index = (left + right)//2
        
        if nums[index] == target:
            response.append(index)
            self.binarySearch(nums, target, response, index+1, right)
            self.binarySearch(nums, target, response, left, index-1)
            
        elif nums[index] < target:
            self.binarySearch(nums, target, response, index+1, right)
        else:
            self.binarySearch(nums, target, response, left, index-1)

        
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        response = []
        self.binarySearch(nums, target, response, 0, len(nums)-1)
        
        if len(response) == 0:
            response = [-1,-1]
        return [min(response), max(response)]