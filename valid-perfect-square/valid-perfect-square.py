class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        product = num
        while product*product > num:
            product = (product + num/product) // 2
            #print(product)
        return product*product == num
            
            
        