class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        n = len(word)
        
        i = 0
        m = 0
        j = 0
        while i < len(abbr):
            if abbr[i].isdigit():
                if abbr[i] == '0': return False
                j = i
                num = 0
                while(j < len(abbr) and abbr[j].isdigit()):
                    num = num*10 + int(abbr[j])
                    j += 1
                m = m + num
                i = j
                #print(m,j)
                
                
            else:
                try:
                    if(word[m]!=abbr[i]) : return False
                    m = m + 1
                    i += 1
                    j += j
                except:
                     return False

                
                
                
        if m == n: return True
        return False
        