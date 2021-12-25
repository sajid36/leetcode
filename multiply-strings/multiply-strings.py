class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total_num1 = 0
        total_num2 = 0
        for i in range (max(len(num1),len(num2))):
            if(i < len(num1)):
                total_num1 = 10*total_num1 + int(num1[i])
            if(i < len(num2)):
                total_num2 = 10*total_num2 + int(num2[i])


        return str(total_num1*total_num2)
        