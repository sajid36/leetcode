class Solution:
    def numberOfMatches(self, n: int) -> int:

        if (n==0): return 0
        matches = 0
        while(n>1):

            if(n%2==0):
                match = int (n/2)
                team = int (n/2)
            else:
                match = int ((n-1)/2)
                team = int ((n-1)/2+1)

            n = team
            matches = matches + match
        return (matches)