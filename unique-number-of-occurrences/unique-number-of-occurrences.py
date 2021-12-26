class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Hash = {}

        for i in arr:
            if i not in Hash.keys():
                Hash[i] = 1
            else: 
                Hash[i] += 1  

        elem = sorted(Hash.values())
        elem2 = set(elem)

        if(len(elem)==len(elem2)):
            return True 
        else:
            return False