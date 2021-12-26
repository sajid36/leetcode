class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = []
        first = 0
        sec = n
        for i in range(n*2):
            if (i % 2) == 0:
                out.append(nums[first])
                first= first + 1
            else:
                out.append(nums[sec])
                sec= sec + 1
        return (out)
        