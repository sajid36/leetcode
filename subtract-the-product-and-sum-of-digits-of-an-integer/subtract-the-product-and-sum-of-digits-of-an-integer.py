class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        product = 1
        while(n>0): 
            digit = n%10
            n = int(n / 10)
            summ = summ + digit 
            product = product * digit
        return (product - summ)
        