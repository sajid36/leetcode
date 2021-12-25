class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        
        
        if m > n:
            diff = m - n
            num2 = '0' * diff + num2
            
        if n > m:
            diff = n - m
            num1 = '0' * diff + num1
        
        
        result = ""
        carry = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        for i in range (len(num1)):
            a = int(num1[i])
            b = int(num2[i])
            
            summ = a + b + carry
            dig = summ%10
            carry = int(summ/10)
            result = result + str(dig)
            
            
        
        if carry > 0:
            result = result + str(carry)
            
        return result[::-1]