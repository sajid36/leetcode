class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = collections.Counter(nums)
        sort_orders = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        
        top = 0
        for key, value in sort_orders:
            if (top >= k): break
            res.append(key)
            top = top + 1

        return res