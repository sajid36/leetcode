class Logger:

    def __init__(self):
        self.d = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.d:
            self.d[message] = 10 + timestamp
            return True
        
        else:
            if timestamp >= self.d[message]:
                self.d[message] = 10 + timestamp
                return True
            else:
                return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)