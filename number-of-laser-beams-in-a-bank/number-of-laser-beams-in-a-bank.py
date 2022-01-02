class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        prev = [-1,0]
        res = 0
        for i in range (len(bank)):
            counter = bank[i].count('1')
            if counter == 0:
                continue
            res = res + counter*prev[1]
            prev = [i,counter]


        return (res)
        