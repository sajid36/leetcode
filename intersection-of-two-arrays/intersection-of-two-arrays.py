class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set(nums1)
        b = set(nums2)
        
        if len(a) < len(b):
            a , b = b, a
            
            
        res = []
        for item in a:
            if item in b:
                res.append(item)
                
                
                
        return res
            
            
        
        