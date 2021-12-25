class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        lenDot = queryIP.count('.')
        lenCol = queryIP.count(':')

        if(lenDot==3 or lenCol==7):
            pass
        else:
            return "Neither"

        res =""
        if lenDot > lenCol:
            iptype = '.'
        else:
            iptype = ':'

        for item in queryIP.split(iptype):
            if iptype == '.':
                if(len(item)==0 or (item[0]=='0' and len(item)>1)): return "Neither"
                try:
                    if 0 <=int(item) <= 255:
                        pass
                    else:
                        return "Neither"
                    res ="IPv4"
                except ValueError:
                    return "Neither"
            else:
                if 1<=len(item)<=4:
                    pass
                else:
                    return "Neither"
                hex_digits = set("0123456789abcdefABCDEF")
                for char in item:
                    if char not in hex_digits:
                        return "Neither"
                res ="IPv6"
                
        return res
        