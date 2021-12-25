class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        length = len(height) - 1
        start = 0

        while (length > start):

            area = max(area, (length - start)*min(height[start], height[length]))
            if(height[start] < height[length]):
                start += 1
            else:
                length -= 1

        return (area)
        