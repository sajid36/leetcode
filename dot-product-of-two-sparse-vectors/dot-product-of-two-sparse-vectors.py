class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}
        
        for i in range(len(nums)):
            # Storing value if non-zero
            if nums[i] != 0:
                self.nums[i] = nums[i]

    def dotProduct(self, vec: 'SparseVector') -> int:
        # Ensure self.nums dict has smaller length
        if len(self.nums) > len(vec.nums):
            return vec.dotProduct(self)
        
        product = 0
        
        for i, n1 in self.nums.items():
            n2 = vec.nums.get(i)
            
            # Ensure n2 is non-zero
            if n2:
                product += n1 * n2

        return product