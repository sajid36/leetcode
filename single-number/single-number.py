class Solution:
    def singleNumber(self, nums: List[int]) -> int:
            summ=0
            for i in nums:
                summ = summ ^ i
                
            return summ
        