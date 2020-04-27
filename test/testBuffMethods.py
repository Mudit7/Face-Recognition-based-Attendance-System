import unittest
import os
from src.entities.subject import Subject
from src.mark_attendance.bufferArg import BufferArg
from src.mark_attendance.bufferManeger import BufferManeger
from src.entities.student import Student
from root_config import ROOT_DIR


class TestBuffMethod(unittest.TestCase):
    
    def setUp(self):
        self.testObjarg=BufferArg()
        self.dirpath='./test/testdir'
        self.expDays=30*6
        self.numSub=2
        os.mkdir(self.dirpath)
        self.testObjarg.setPath(self.dirpath)
        self.testObjarg.setExpirationTime(self.expDays)
        self.testObjarg.setNumOfSub(self.numSub)
        self.testObj=BufferManeger(self.testObjarg)
        subCode_list=[101,102,103,104]
        for i in subCode_list:
            self.testObj.getSubject(i)
        
    def test_dirExist(self):
        self.assertTrue(os.path.exists(self.dirpath))
        
    def test_numFileGenerated(self):
        file_list=os.listdir(self.dirpath)
        numFile=len(file_list)
        self.assertEqual(numFile,self.numSub+2)
        
    def test_ConutFileExistance(self):
        file_path=self.dirpath+'/count'
        self.assertTrue(os.path.exists(file_path))
        
    def test_indexFileExistance(self):
        file_path=self.dirpath+'/index'
        self.assertTrue(os.path.exists(file_path))
    
    def test_currenctSubExistance(self):
        cur_list=[103,104]
        for file_code in cur_list:
            fname='a_'+str(file_code)
            file_path=self.dirpath+'/'+fname
            self.assertTrue(os.path.exists(file_path))
    
    def test_LruRemoval(self):
      cur_list=[101,102]
      for file_code in cur_list:
            fname='a_'+str(file_code)
            file_path=self.dirpath+'/'+fname
            self.assertFalse(os.path.exists(file_path))
      
    def tearDown(self):
        os.system('rm -r ./test/testdir')
        
        
if __name__ == '__main__':
    unittest.main()
