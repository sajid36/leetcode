class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        #print("muhaha")
        maximum = -2147483648
        nums.insert(0,maximum)
        nums.append(maximum)
        n = len(nums) - 1
        #print(nums)
        for i in range(1,len(nums)-1):
            if nums[i] >= nums[i+1] and nums[i] >= nums[i-1]:
                return (i-1)
            if nums[n-i] >= nums[n+1-i] and nums[n-i] >= nums[n-i-1]:
                return (n-i-1)
                
                
                
            
            
        
            
        