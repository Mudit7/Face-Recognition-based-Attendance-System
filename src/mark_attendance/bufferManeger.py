from src.entities.subject import Subject
from src.mark_attendance.dataloader import DataLoader
from src.mark_attendance.bufferArg import BufferArg
import os
import pickle
import datetime

#number of files stored
class BufferManeger:
    
    directoryPath=None
    subjectLoader=None
    indexFilePath=None
    countFilePath=None
    indexDict=None
    subject_count=None
    count_theshold=None
    exp_day=None
    
    
    #constructor needs to be changed
    def __init__(self,buffArg):
        self.directoryPath=buffArg.getPath()
        self.subjectLoader=DataLoader()
        self.setIndexFilePathTo('index')
        self.setCountFilePathTO('count')
        self.loadCount()
        self.exp_days=buffArg.getExpirationTime()
        self.count_theshold=buffArg.getNumOfSub()
        
        
    def getSubject(self,subCode):
        self.initIndex()
        if self.isSubPresent(subCode):
            tempSub=self.getBufferedSubject(subCode)
        else:
            tempSub=self.getNewSubject(subCode)
            self.saveOnBuffer(tempSub)
        return tempSub
    
    def saveOnBuffer(self,sub):
        self.updateSubPath(sub)
        self.updateIndex(sub.getSubjectCode())
        self.incSubCounter()
        if  self.countUnStable():
            oldSubCode=self.getOldestSub()
            self.delSubPath(oldSubCode)
            del self.indexDict[oldSubCode]
            self.updateIndexPath()
            self.decSubCounter()
        self.updateCountPath()
    
    
    
    def getSubPath(self,subCode):
        return self.directoryPath+'/a_'+str(subCode)
        
    def updateSubPath(self,sub):
        subCode=sub.getSubjectCode()
        path=self.getSubPath(subCode)
        try:
            f=open(path,'wb')
            pickle.dump(sub,f)
            f.close()
        except OSError:
            raise ValueError('problem in saving to buffer')

    
    def updateIndex(self,subCode):
        self.indexDict[subCode]=datetime.datetime.now().date()
        self.updateIndexPath()
        
    def delSubPath(self,subCode):
        path=self.getSubPath(subCode)
        os.remove(path)
        
    def initIndex(self):
        if not self.isIndexPresent():
            self.createIndex()
        self.loadIndex()
            
    def isFileExpired(self,subCode):
        store_date=self.getValidDate(subCode)
        curr_date=datetime.datetime.now().date()
        diff=(store_date-curr_date).days
        if diff < self.exp_days:
            return False
        else:
            return True
    
    def getRefresedSub(self,subCode):
        tempSub=self.getNewSubject(subCode)
        self.replaceInBuffer(tempSub)
        return tempSub
    
    def getBufferedSubject(self,subCode):
        if self.isFileExpired(subCode):
            tempSub=self.getRefresedSub(subCode)
        else:
            tempSub=self.loadFromBuffer(subCode)
        return tempSub
    
    def getNewSubject(self,subCode):
        print("subject code", subCode)
        tempSub=self.subjectLoader.getSubject(subCode)
        return tempSub
    
    def replaceInBuffer(self,sub):
        self.decSubCounter()
        self.saveOnBuffer(sub)
        
    def getOldestSub(self):
        old_date=datetime.date(2200,1,1)
        old_subCode=None
        for k in self.indexDict.keys():
            t_date=self.indexDict[k]
            if t_date < old_date:
                old_date=t_date
                old_subCode=k
        return old_subCode
                
    def setSubCounter(self):
        self.subject_count=0
    
    def incSubCounter(self):
        self.subject_count+=1
        
    def decSubCounter(self):
        self.subject_count-=1
        
    def countUnStable(self):
        if self.count_theshold < self.subject_count:
            return True
        else:
            return False
        
    def setIndexFilePathTo(self,filename):
        self.indexFilePath=self.directoryPath+'/'+filename
    
    def setCountFilePathTO(self,filename):
        self.countFilePath=self.directoryPath+'/'+filename
        
    def createIndex(self):
        f=open(self.indexFilePath,'w')
        f.close()
    
    def isIndexPresent(self):
        if os.path.isfile(self.indexFilePath):
            return True
        else:
            return False
      
    def loadIndex(self):
        try:
            f=open(self.indexFilePath,'rb')
            self.indexDict=pickle.load(f)
            f.close()
        except EOFError:
            self.indexDict={}
            
    def loadCount(self):
        try:
            f=open(self.countFilePath,'rb')
            self.subject_count=pickle.load(f)
            f.close()
        except OSError:
            self.subject_count=0
           
    def updateIndexPath(self):
        try:
            f=open(self.indexFilePath,'wb')
            pickle.dump(self.indexDict,f)
            f.close()
        except OSError:
            raise ValueError('unable to write to the file')
            
    def updateCountPath(self):
        try:
            f=open(self.countFilePath,'wb')
            pickle.dump(self.subject_count,f)
            f.close()
        except OSError:
            raise ValueError('unable to write to the file')
    
    def isSubPresent(self,subCode):
        if subCode in self.indexDict.keys():
            return True
        else:
            return False
     
    def getValidDate(self,subCode):
        if not self.isSubPresent(subCode):
            raise ValueError('subject is not present in the buffer')
        return self.indexDict[subCode]
            
    def loadFromBuffer(self,subCode):
        path=self.directoryPath+'/a_'+str(subCode)
        try:
            f=open(path,'rb')
            tempSub=pickle.load(f)
            f.close()
            return tempSub
        except OSError:
            raise ValueError('unable to read the file')
