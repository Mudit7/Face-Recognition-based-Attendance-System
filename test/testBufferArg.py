import unittest
from bufferArg import BufferArg
class TestBufferArg(unittest.TestCase):
    
    def setUp(self):
        self.testobj=BufferArg()
        self.path='/temp_path'
        self.exp_date=45
        self.numofsub=15
        self.testobj.setPath(self.path)
        self.testobj.setExpirationTime(self.exp_date)
        self.testobj.setNumOfSub(self.numofsub)
        
    def test_getPath(self):
        self.assertEqual(self.testobj.getPath(),self.path)
        
    def test_getexptime(self):
        self.assertEqual(self.testobj.getExpirationTime(),self.exp_date)
        
    def test_getnumofsub(self):
        self.assertEqual(self.testobj.getNumOfSub(),self.numofsub)
        
if __name__ == '__main__':
    unittest.main()