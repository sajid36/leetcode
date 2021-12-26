class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        c = collections.Counter(digits)
        res = []
        for i in range (100, 999, 2):
            temp = list(str(i))
            c_temp = collections.Counter(temp)
            if(c_temp[temp[0]] <= c[int(temp[0])]):
                if(c_temp[temp[1]] <= c[int(temp[1])]):
                    if(c_temp[temp[2]] <= c[int(temp[2])]):
                        res.append(i)

        return (res)
        