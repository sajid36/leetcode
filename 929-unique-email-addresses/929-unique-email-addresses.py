class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        res = set()
        
        for item in emails:
            if '.' in item:
                at = item.index("@")
                temp = item[:at]
                temp = temp.replace('.', '')
                if '+' in temp:
                    plus = temp.index("+")
                    temp = temp[:plus]
                temp = temp+item[at:]
                #print(temp)
                
                res.add(temp)
                
                
                
        return len(res)
        