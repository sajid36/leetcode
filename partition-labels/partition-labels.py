class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        flag = 0
        part = {}
        uniq = set (s)
        seen = []
        res = []
        for item in s:
            if item not in seen:
                seen.append(item)
                part[item] = list()
                part[item].append(s.index(item))
                part[item].append(s.rfind(item))


        #print(part)


        first_value = list(part.values())[0]
        start = first_value[0]
        end = first_value[1]


        for key, val in part.items():
            #print("")
            #print("")
            #print(key, val)
            #print(start, end)
            if val[0] < start:
                #print('a updating')
                start = val[0]
            if val[0] >= start and val[0] <=end:
                if val[1] > end:
                    #print('b updating')
                    end = val[1]
            #print('--')
            #print(val[0], end)
            if val[0] > end:
                flag = 1
                #print('partition needed from')
                #print(start, end)
                res.append(end-start+1)
                start = val[0]
                end = val[1]

        if flag == 0:
            #print('partition not possible')
            return ([len(s)])
        else:
            length = len(s)
            for item in res:
                length = length - item
            res.append(length)

        return (res)