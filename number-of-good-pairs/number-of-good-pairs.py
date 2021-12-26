class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = {}
        for idx, val in enumerate(nums):
            if val not in result:
                result[val] = [idx]
            else:
                result[val].append(idx)

        #print(result)
        total = 0
        for key, val in result.items():
            a = len(val)
            b = len(val) - 1
            total = total + (a*b)/2

        return (int(total))
        