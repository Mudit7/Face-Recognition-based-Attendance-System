import unittest
from group import Group

class TestStudent(unittest.TestCase):
    
    def setUp(self):
        self.name='nabhiraj'
        self.code=62
        self.img=None
        self.testobj=Group(self.code,self.name,self.img)
        
    def test_getName(self):
        print('group name')
        self.assertEqual(self.testobj.getSubjectName(),self.name)
    
    def test_getRollNo(self):
        print('grou roll number')
        self.assertEqual(self.testobj.getSubjectCode(),self.code)
    
    def test_getImage(self):
        print('group image')
        self.assertEqual(self.testobj.getGroupImage(),self.img)
        
if __name__ == '__main__':
    unittest.main()