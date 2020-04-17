import unittest
from subject import Subject

class TestSubject(unittest.TestCase):
    
    def setUp(self):
        self.code=1
        self.name='aps'
        self.slist=None
        self.testobj=Subject(self.code,self.name,self.slist)
        
    def test_getSubjectName(self):
        print('subject name')
        self.assertEqual(self.testobj.getSubjectName(),self.name)
    
    def test_getSubjectCode(self):
        print('subject code')
        self.assertEqual(self.testobj.getSubjectCode(),self.code)
        
    def test_getSudentList(self):
        print('student list')
        self.assertEqual(self.testobj.getStudentList(),self.slist)
        
        
        
if __name__ == '__main__':
    unittest.main()
        
        