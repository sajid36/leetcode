class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        
        if n>m:
            nums1, nums2 = nums2, nums1
        res = []
        counter = 0
        for item in nums1:
            if item in nums2:
                res.append(item)
                nums2.remove(item)
                counter = counter + 1
            if(len(nums2)==0):
                break
                
                
        return res
        