class Solution:
    def minimumBuckets(self, street: str) -> int:
        length  = len (street)
        numH = 0
        numDot = 0
        
        if length == 1:
            if street[0] == '.': return 0
            else:
                return -1
        if length > 1:
            if street[0] == 'H' and street[1] == 'H': return -1
            if street[length-1] == 'H' and street[length-2] == 'H': return -1
        
        i = 0
        res = 0
        while i <= length - 1:
            if street[i] == '.' and numDot==0:
                numDot = 1
            elif street[i] == 'H' and numH==0:
                numH = 1
                
            else:
                if street[i] == 'H':
                    if i - 1 >= 0 and i + 1 <= length - 1 and street[i-1] == 'H' and street[i+1] == 'H':
                            return -1
                    elif i + 2 <= length - 1 and street[i+1] == '.' and street[i+2] == 'H':
                            res = res + 1
                            i = i + 3
                    elif i + 1 <= length - 1:
                        if street[i+1] == '.':
                            res = res + 1
                            i = i + 2
                        else:
                            i = i + 1
                else:
    
                    if i + 3 <= length - 1 and street[i+1]=='H' and street[i+2]=='.' and street[i+3]=='H':
                         
                            res = res + 1
                            i = i + 4
                    else:
                   
                        if i + 1 <= length - 1:

                            if street[i+1] == 'H':
                                res = res + 1
                                i = i + 2
                            else:
                                i = i + 1
                        else:
                            i = i + 1    
        return (res)