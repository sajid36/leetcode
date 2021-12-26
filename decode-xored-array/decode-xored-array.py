class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = []
        result.append(first)

        for i in range (len(encoded)):
            a = encoded[i] ^ first
            result.append(a)
            first = a
        return(result)