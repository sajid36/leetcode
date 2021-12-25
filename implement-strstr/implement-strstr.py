class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 or (len(needle) == 0 and len(haystack) == 0): return 0
        if len(haystack) == 0: return -1
        if needle in haystack:
            return (haystack.index(needle))
        return -1