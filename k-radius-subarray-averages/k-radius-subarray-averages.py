from statistics import mean

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        for i, num in enumerate(nums):
            if i-k < 0 or i+k >= n:
                res.append(-1)
            else: # k<=i<n-k
                if i-k == 0:
                    curSum = sum(nums[:i+k+1])
                else:
                    curSum -= nums[i-k-1] # remove the first element of the previous window
                    curSum += nums[i+k] # add the new element that is the last element of the current window
                res.append(curSum//(2*k+1))
        return res
        