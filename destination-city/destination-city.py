class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen = []
        for a,b in paths:
            seen.append(a)
            seen.append(b)
        unique = set(seen)
        #print(unique)

        for a,b in paths:
            if a in unique:
                unique.remove(a)

        return("".join(unique))
        