class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = []
        dup = []
        result= 0
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique.append(nums[i])
                result = result + nums[i]
            else:
                if nums[i] not in dup:
                    dup.append(nums[i])
                    result = result - nums[i]
        return (result)
        