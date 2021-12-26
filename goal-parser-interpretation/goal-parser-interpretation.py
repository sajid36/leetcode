class Solution:
    def interpret(self, command: str) -> str:
        s = 0
        out = ""
        while (s<len(command)):
            print(s)
            if (command[s] == 'G'):
                out = out + 'G'
                s = s + 1
            elif (command[s] == '('):
                if (command[s+1] == ')'):
                    out = out + 'o'
                    s=s + 2
                else:
                    out = out + 'al'
                    s= s + 4
        return (out)
        