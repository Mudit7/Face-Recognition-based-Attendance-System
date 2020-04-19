class Group:
    
    subjectCode=None
    subjectName=None
    groupImage=None
    
    def __init__(self,code,name,img):
        self.subjectCode=code
        self.subjectName=name
        self.groupImage=img
    
    def getSubjectCode(self):
        return self.subjectCode
    
    def getSubjectName(self):
        return self.subjectName
    
    def getGroupImage(self):
        return self.groupImage
    
    