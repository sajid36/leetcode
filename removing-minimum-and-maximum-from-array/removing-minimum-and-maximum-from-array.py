class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        maxi = max(nums)
        mini = min(nums)
        index_maxi= nums.index(maxi)
        index_mini= nums.index(mini)

        res = min(index_maxi+1, len(nums)-index_maxi)
        res2 = min(index_mini+1, len(nums)-index_mini)

        flag = 0
        cost = 0
        if (res<=res2):
            flag = 1
            if index_maxi+1 <= len(nums)-index_maxi:
                cost = cost + index_maxi+1
                nums = nums[index_maxi+1:]
            else:
                cost = cost + len(nums)-index_maxi
                nums = nums[:index_maxi]
        else:
            if index_mini+1 <= len(nums)-index_mini:
                cost = cost + index_mini+1
                nums = nums[index_mini+1:]
            else:
                cost = cost + len(nums)-index_mini
                nums = nums[:index_mini]

        if flag ==1:
            #mini
            index_mini= nums.index(mini)
            if index_mini+1 <= len(nums)-index_mini:
                cost = cost + index_mini+1
                nums = nums[index_mini+1:]
            else:
                cost = cost + len(nums)-index_mini
                nums = nums[:index_mini]

        else:
            #maxi
            index_maxi= nums.index(maxi)
            if index_maxi+1 <= len(nums)-index_maxi:
                cost = cost + index_maxi+1
                nums = nums[index_maxi+1:]
            else:
                cost = cost + len(nums)-index_maxi
                nums = nums[:index_maxi]



        return (cost)
        