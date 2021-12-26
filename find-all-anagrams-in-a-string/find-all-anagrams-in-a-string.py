class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left =  0
        right = len(p) - 1
        res = []
        pcounter = collections.Counter(p)
        while right < len(s):
            tempcounter = collections.Counter(s[left:right+1])
            if(tempcounter==pcounter):
                res.append(left)
            left += 1
            right +=1
            
            
        return res
            
            