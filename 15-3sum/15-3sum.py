class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)

        if l <= 2:
            return []

        nums.sort()
        print(nums)
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            left = i + 1
            right = l - 1

            while left < right:
                sum3 = a + nums[left] + nums[right]
                if sum3 > 0:
                    right = right - 1
                elif sum3 < 0:
                    left = left + 1
                else:
                    res.append([a , nums[left], nums[right]])
                    left = left + 1
                    while nums[left] == nums [left - 1] and left < right:
                        left = left + 1
        return (res)
        