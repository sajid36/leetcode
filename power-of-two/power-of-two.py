class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        elif (n%2!=0):
            return False
        else:
            res = 1
            for i in range(32):
                if(res > n):
                    return False
                else:
                    if (res==n):
                        return True
                    else:

                        res = res * 2

