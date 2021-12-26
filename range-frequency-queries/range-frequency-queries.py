from bisect import bisect_left
from bisect import bisect_right
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.result = {}
        for i in range (len(arr)):
            if arr[i] not in self.result.keys():
                self.result[arr[i]] = list()
                self.result[arr[i]].append(i)
            else:
                self.result[arr[i]].append(i)
        #print(self.result)
                
        

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.result.keys():
            return 0
        else:
            a = bisect_left(self.result[value], left)
            b = bisect_right(self.result[value], right)
            #print(a)
            #print(b)
            #temp = sorted(self.result[value])
            
            #counter = 0
            #for item in temp:
            #    if(item > right):
            #        break
            #    if (left<=item<=right):
            #        counter = counter + 1
                    
        return (b - a)
        


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)