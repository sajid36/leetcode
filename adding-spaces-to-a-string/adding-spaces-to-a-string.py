class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        result = ""
        set_space = set(spaces)
        for i, char in enumerate(s):
            if i in set_space: 
                result = result +  " "
            result = result + char
        return result
        