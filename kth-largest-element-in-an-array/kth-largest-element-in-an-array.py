class Solution:        
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        
        for item in nums:
            heapq.heappush(queue, item)
            if len(queue) > k:
                heapq.heappop(queue)
                
        return (queue[0])