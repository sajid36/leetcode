class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        fWealth = 0
        for x in range (len(accounts)):
            wealth = 0
            for y in range (len(accounts[x])):
                wealth = wealth + accounts[x][y]
            if(wealth>fWealth):
                fWealth = wealth
        return fWealth
        