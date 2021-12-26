class Solution:
    def modifyString(self, s: str) -> str:
        out = ""
        if(len(s)==1):
            if(s[0]=='?'):
                return 'a'
            else:
                return s 
        else:
            for x in range (len (s)): 
                #print("char in consideration : ", s[x])
                #print("x in consideration : ", x)
                if(s[x]=='?'):
                    if(x==0):
                        if(s[x+1]=='?'):
                            out = out + 'a'
                        else:
                            temp = ord(s[x+1])-96
                            if(25>=temp>=1):
                                temp = temp + 1
                                out = out + chr(temp+96)
                            else: 
                                temp = temp - 1
                                out = out + chr(temp+96)
                        print("-",out)
                    elif(x>0 and x<(len(s))-1):
                        if(s[x+1]=='?'):
                            temp = ord(out[x-1])-96
                            print(temp)
                            if(25>=temp>=1):
                                temp = temp + 1
                                out = out + chr(temp+96)
                            else: 
                                temp = temp - 1
                                out = out + chr(temp+96)
                            print("--",out)
                        else:
                            temp = ord(out[x-1])-96
                            temp2 = ord(s[x+1])-96
                            print(temp)
                            print(temp2)
                            if(abs(temp-temp2) == 0):
                                if(temp == 26):
                                    temp = temp - 1
                                    out = out + chr(temp+96)
                                else:
                                    temp = temp + 1
                                    out = out + chr(temp+96)                  
                            elif(abs(temp-temp2) == 1):
                                if(temp==26 or temp2 == 26):
                                    temp = temp - 2
                                    out = out + chr(temp+96)
                                else:
                                    if(temp<temp2):
                                        temp = temp + 2
                                        out = out + chr(temp+96)
                                    else:
                                        temp = temp2 + 2
                                        out = out + chr(temp+96)
                            else:
                                if(temp<temp2):
                                    temp = temp + 1
                                    out = out + chr(temp+96)
                                else:
                                    temp = temp2 + 1
                                    out = out + chr(temp+96)
                            print("---",out)       
                    elif(x==(len(s))-1):
                        temp = ord(out[x-1])-96
                        if(25>=temp>=1):
                                temp = temp + 1
                                out = out + chr(temp+96)
                        else: 
                            temp = temp - 1
                            out = out + chr(temp+96)
                        print("----",out)

                else:
                    out = out + s[x]
            return (out)
        