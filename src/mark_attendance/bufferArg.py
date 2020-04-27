class BufferArg:
    path=None
    expDays=None
    numOfSub=None
    
    #def __init__(self,path,expDays,numOfSub):
    #    self.path = path
    #    self.expDays = expDays
    #    self.numOfSub = numOfSub

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
        
        
        
        