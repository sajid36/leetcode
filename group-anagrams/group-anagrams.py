class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}
        for item in strs:
            key = ' '.join(sorted(item))
            if key not in result.keys():
                result[key] = [item]
            else:
                result[key].append(item)


        return (result.values())