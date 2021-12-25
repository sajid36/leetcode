class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        startSign = '+'
        res = []
        s+='+'
        for ch in s:
            if ch.isdigit():
                num = num*10 + int(ch)
            elif ch == " ":
                continue
            else:
                if startSign == '+':
                    res.append(num)
                elif startSign == '-':
                    res.append(-num)
                elif startSign == '*':
                    a = res.pop()
                    res.append((a*num))
                elif startSign == '/':
                    a = res.pop()
                    res.append(int(a/num))
                    
                num = 0
                startSign = ch
        return sum(res)
                
                    
                
                
            