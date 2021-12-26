class Solution:
    def defangIPaddr(self, address: str) -> str:
        out = address.replace(".", "[.]")
        return out