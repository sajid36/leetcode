class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        Hash = {}

        for i in A:
            if i not in Hash.keys():
                Hash[i] = 1
            else: 
                return (i)
        