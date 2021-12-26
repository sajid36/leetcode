class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out = []
        for x in range(len(nums)):
            count = 0
            for y in range(len(nums)):
                if(x==y):
                    continue
                else:
                    if(nums[x]>nums[y]):
                        count = count + 1
            out.append(count)
        return out
        