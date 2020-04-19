from src.entities.student import Student
class Subject:
    
    subjectCode=None
    subjectName=None
    studentList=[Student(None,None,None),Student(None,None,None)]
    
    def __init__(self,code,name,slist):
        self.subjectCode=code
        self.subjectName=name
        self.studentList=slist
        
    def getSubjectCode(self):
        return self.subjectCode
    
    def getSubjectName(self):
        return self.subjectName
    
    def getStudentList(self):
        return self.studentList
