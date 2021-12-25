class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0: 
            sign = sign * (-1) 
            dividend = dividend * (-1)
        if divisor < 0: 
            sign = sign * (-1) 
            divisor = divisor * (-1)
        if divisor==1: return max(pow(-2, 31) , min(dividend*sign, pow(2, 31) - 1))
        

        div = str(dividend)
        l_divisor = len(str(divisor))
        res = ""
        carry = '0'
        for i in range (0, len(div), l_divisor):
            temp_dividend = int(carry + div[i:i+l_divisor])
            counter = 0
            while temp_dividend >= divisor:
                temp_dividend = temp_dividend - divisor
                carry = str(temp_dividend)
                counter = counter + 1
            if(temp_dividend < divisor):
                carry = str(temp_dividend)
                
            res = res + str(counter)
        res = int(res)
        return max(pow(-2, 31) , min(res*sign, pow(2, 31) - 1))