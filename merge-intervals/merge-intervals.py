class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = []
        res.append(intervals[0])
        j = 0
        for i in range (1, len(intervals)):
            if res[j][0]<=intervals[i][0]<=res[j][1]:
                res[j] = [min(res[j][0],intervals[i][0]), max(res[j][1],intervals[i][1])]
            else:
                res.append(intervals[i])
                j+=1
        return(res)
                
            