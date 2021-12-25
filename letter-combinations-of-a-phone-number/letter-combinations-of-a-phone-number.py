class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        temp = [] 
        ret = []
        dicts = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        #print(digits)
        if len(digits)==0:
            #print("here")
            return (ret)
        if len(digits)==1:
            #print("here")
            for ch in dicts[digits]:
                ret.append(ch)
            return (ret)


        counter = 1
        #print("here")
        for ch in digits:
            counter = counter * len(dicts[ch])
            temp.append(dicts[ch])

        #print(temp)
        for i in range(len(temp)):
            x = []
            for j in range(len(temp[i])):
                x.append(temp[i][j])
            ret.append(x)

        result=[]
        if len(digits) == 2:
            result.append(list(itertools.product(ret[0],ret[1])))
        if len(digits) == 3:
            result.append(list(itertools.product(ret[0],ret[1],ret[2])))
        if len(digits) == 4:
            result.append(list(itertools.product(ret[0],ret[1],ret[2],ret[3])))


        result_combination = []

        for i in range (counter):
            tempStr = ""
            for j in range (len(digits)):
                tempStr = tempStr + result[0][i][j]
            result_combination.append(tempStr)
        return (result_combination)
        