class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        if len(nums) == 1:
            return [nums[:]]
        
        
        for i in range(len(nums)):
            n = nums.pop(0)
            
            perms = self.permuteUnique(nums)
            
            for perm in perms:
                perm.append(n)   
            
            
            #print(perms)
            result.extend(perms)
            nums.append(n)
            
            
        seen = []
        for item in result:
            if item not in seen:
                seen.append(item)

                
        return seen