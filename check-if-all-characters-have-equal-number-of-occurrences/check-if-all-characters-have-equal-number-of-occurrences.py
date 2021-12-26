class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        unique = set(s)
        count = collections.Counter(s)
        if max(count.values()) == min(count.values()):
            return True
        else:
            return False
        