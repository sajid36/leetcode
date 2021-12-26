class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        for item in points:
            value = math.sqrt(pow(item[0],2) + pow(item[1],2))
            heapq.heappush(queue, [value,item])
 
            
            
            
        result = []
        for i in range(k):
            answer = heapq.heappop(queue)[1]
            result.append(answer)
        return (result)
        