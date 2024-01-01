import time
from time import localtime

class MyTimer():

    def begin(self):
        self.begin = time.localtime()
        print("计时器开始记时！")
        print(self.begin)
        return self.begin
        

    def end(self):
        self.end = time.localtime() 
        print("计时器停止记时！")
        print(self.end)
        return self.end

    
