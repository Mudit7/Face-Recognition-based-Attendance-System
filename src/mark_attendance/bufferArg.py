class BufferArg:
    path=None
    expDays=None
    numOfSub=None
    
    def setPath(self,path):
        self.path=path
        
    def setExpirationTime(self,days):
        self.expDays=days
        
    def setNumOfSub(self,num):
        self.numOfSub=num
        
    def getPath(self):
        return self.path
    
    def getExpirationTime(self):
        return self.expDays
    
    def getNumOfSub(self):
        return self.numOfSub
        
        
        
        