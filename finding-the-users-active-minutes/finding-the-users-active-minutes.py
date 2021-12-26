class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        work = {}
        seen = []
        answer = [0]*k
        for item in logs:
            if item[0] not in seen:
                seen.append(item[0])
                work[item[0]] = list()
                work[item[0]].append(item[1])
            else:
                work[item[0]].append(item[1])

        #print(work)


        for key, val in work.items():
            val = set(val)
            count = len(val)
            answer[count-1] = answer[count-1] + 1 


        return (answer)
        