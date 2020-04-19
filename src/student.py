class Student:
    
    studentName=None
    studentRollNo=None
    studentImg=[]
    
    def __init__(self,rollNo,name,img):
        self.studentImg=img
        self.studentRollNo=rollNo
        self.studentName=name
    
    def getName(self):
        return self.studentName
    
    def getRollNo(self):
        return self.studentRollNo
    
    def getImage(self):
        return self.studentImg
    
    