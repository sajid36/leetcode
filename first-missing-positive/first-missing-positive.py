class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==1:
            if nums[0]==1:
                return 2
            else:
                return 1
        if 1 not in nums:
            return 1
        
        length = len(nums)
        seen =["#"]*length
        #print(seen)
        
        for item in nums:
            if item >=1 and item <=length:
                seen[item -1] = item
        for i in range(length):
            if seen[i] == "#":
                return i+1
        return length+1

        