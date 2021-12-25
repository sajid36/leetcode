class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        for i in range (1, len(nums)):
            res[i] = nums[i-1]*res[i-1]

            
        print(res)
        right = 1
        for i in range (len(nums)-1,-1,-1):
            print(i)
            res[i] = res[i]*right
            right = right * nums[i]

        return (res)
        