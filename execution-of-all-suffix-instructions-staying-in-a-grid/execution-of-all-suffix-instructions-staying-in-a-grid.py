class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        initx = startPos[0]
        inity = startPos[1]
        answer = [0] * len(s)

        for i in range (len(s)):
            tempy, tempx = inity, initx
            counter = 0
            for j in range (i, len(s)):
                if(s[j]=='R'):
                    tempy = tempy + 1
                    if(tempy > n - 1):
                        break
                elif(s[j]=='L'):
                    tempy = tempy - 1
                    if(tempy < 0):
                        break
                elif(s[j]=='D'):
                    tempx = tempx + 1
                    if(tempx > n - 1):
                        break
                elif(s[j]=='U'):
                    tempx = tempx - 1
                    if(tempx < 0):
                        break

                counter = counter + 1


            answer[i] = counter




        return (answer)
        