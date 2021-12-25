class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0: return 0
        maxlen = 0
        dic = {}
        j = 0
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
            while len(dic) > k:
                dic[s[j]] -= 1
                if dic[s[j]] == 0:
                    del dic[s[j]]
                j += 1
            maxlen = max(maxlen, i-j+1)
        return maxlen
        