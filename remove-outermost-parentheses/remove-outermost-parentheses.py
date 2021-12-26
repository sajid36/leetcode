class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        countS=0
        countE=0
        final = ""
        for i in S:
            #print (i)
            if(i=='('):
                result.append(i)
                countS=countS + 1
            else:
                result.append(i)
                countE=countE + 1

            if(countS==countE):
                #print(result)
                res = result[1:(len(result)-1)]
                resStr = ''.join(res)
                final = final + resStr
                result.clear()
                #print(res)

        return(final)
        