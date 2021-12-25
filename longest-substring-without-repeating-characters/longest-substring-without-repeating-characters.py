class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        res = 0

        for i in range (len(s)):
            if s[i] in seen:
                left = max(left, seen[s[i]] + 1)
            seen[s[i]] = i
            res = max(res, i - left + 1)


        return (res)
        