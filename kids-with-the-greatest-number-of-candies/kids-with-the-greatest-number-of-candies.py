class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        out = []
        for x in range (len(candies)):
            if(candies[x]+extraCandies >= maxi):
                out.append(True)
            else: 
                out.append(False)
        return out
        