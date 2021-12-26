class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        res = {}
        result = []
        for val in set(nums1):
            res[val]=1
        print(res)
        for val in set(nums2):
            if val not in res.keys():
                res[val]=1
            else:
                res[val]=2
                result.append(val)
        print(res)
        for val in set(nums3):
            if val not in res.keys():
                continue
            else:
                if res[val]==1:
                    result.append(val)


        return (result)
        