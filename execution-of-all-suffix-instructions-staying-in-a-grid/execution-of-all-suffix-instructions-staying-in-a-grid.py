class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        d = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
        ans = [0] * len(s)
        for i in range(len(s)):
            [x, y] = startPos
            for j in range(i, len(s)):
                x += d[s[j]][0]
                y += d[s[j]][1]
                if 0 <= x < n and 0 <= y < n:
                    ans[i] += 1
                else:
                    break
        return ans