class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sortedList = sorted(nums)
        #print(sortedList)
        positive = [x for x in sortedList if x>=0]
        #print(positive)
        length = len(positive)

        count = 0
        result = 1
        flag = 0
        for i in range (length):
            if(positive[i]>0):
                count = 1

            if(positive[i]==1):
                flag = 1

            if (i==length-1):
                result = positive[i] + 1
                print("set eq")
                break
            if(positive[i+1] - positive[i] > 1):
                result = positive[i] + 1
                #print(positive[i+1])
                #print(positive[i])
                #print("set not eq")
                break


        if (count ==0):
            return 1
        elif(flag == 0):
            return 1
        else: 
            return (result)
        