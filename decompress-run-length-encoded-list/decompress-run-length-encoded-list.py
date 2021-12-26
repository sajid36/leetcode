class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out = []
        for x in range (0, len(nums), 2):
            print(x)
            feq = nums[x]
            pos = x
            val = nums[pos+1]
            
            print(val)
            for y in range (feq):
                out.append(val)
        return (out)