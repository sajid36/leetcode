class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        work = sorted(nums1+nums2)
        length = len(work)

        if(length%2==0):
            mid = int(length/2)
            median = (work[mid-1]+work[mid])/2
        else:
            mid = int(length/2)
            median = (work[mid])

        return (median)
        