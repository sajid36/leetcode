class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = {}
        res = []
        for i in range (len(groupSizes)):
            if (groupSizes[i] not in group.keys()):
                group[groupSizes[i]] = list()
                group[groupSizes[i]].append(i)
            else:
                group[groupSizes[i]].append(i)

        group = sorted(group.items())
        #print(group)

        #print(res)


        for key, value in group:
            if key >= len(value):
                res.append(value)
            else:
                while (len(value) > 0):
                    res.append(value[0:key])
                    value = value [key:] 


        return (res)
        