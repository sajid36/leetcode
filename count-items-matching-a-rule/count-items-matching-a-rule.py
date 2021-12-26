class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            key = 0
        if ruleKey == "color":
            key = 1
        if ruleKey == "name":
            key = 2

        count = 0
        for item in items:
            if(item[key]==ruleValue):
                count = count + 1

        return (count)
        