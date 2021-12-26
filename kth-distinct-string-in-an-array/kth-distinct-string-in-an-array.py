class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = collections.Counter(arr)
        sortCount = sorted(count.items(), key=lambda item: item[1])
        print(sortCount)

        if(len(sortCount))==0:
            return ("")
        if(len(sortCount) < (k)): 
            return ("")
        else:
            if(sortCount[k-1][1]==1):
                return (sortCount[k-1][0])
            else:
                return ("")