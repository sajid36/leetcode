class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        hashmap = {}
        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in hashmap.keys():
                result.append(hashmap[rem])
                result.append(i)
            else:
                hashmap[nums[i]] = i
        return result
        