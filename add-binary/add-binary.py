class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        len_a = len(a)
        len_b = len(b)
        carry = '0'
        
        a = a[::-1]
        b = b[::-1]
        for i in range(max(len_a,len_b)):
            if(i >=len_a):
                digit_a = '0'
            else:
                digit_a = a[i]
            
            if(i >=len_b):
                digit_b = '0'
            else:
                digit_b = b[i]
                
                
            #print(digit_a,digit_b)
                
            if(digit_a == '1' and digit_b == '1' and carry=='1'):
                carry = '1'
                res = res + '1'
                
                
                
                
            elif (digit_a == '1' and digit_b == '1' and carry=='0'):
                carry = '1'
                res = res + '0'
                
            elif (digit_a == '1' and digit_b == '0' and carry=='1'):
                carry = '1'
                res = res + '0'
                
            elif (digit_a == '0' and digit_b == '1' and carry=='1'):
                carry = '1'
                res = res + '0'
                
                
                
                
            elif (digit_a == '0' and digit_b == '0' and carry=='1'):
                carry = '0'
                res = res + '1'
                
            elif (digit_a == '0' and digit_b == '1' and carry=='0'):
                carry = '0'
                res = res + '1'
                
            elif (digit_a == '1' and digit_b == '0' and carry=='0'):
                carry = '0'
                res = res + '1'
                
                
                
                
            elif (digit_a == '0' and digit_b == '0' and carry=='0'):
                carry = '0'
                res = res + '0'
                
                
                
            #print(res)
                
        if carry == '1':
            res = res + '1' 
        return res[::-1]
                
            
            
