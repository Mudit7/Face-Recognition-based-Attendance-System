import unittest
from src.mark_attendance.faceMatcher import FaceMatcher
from src.entities.group import Group
from root_config import ROOT_DIR
import cv2


class TestFaceMatcher(unittest.TestCase):
    def setUp(self):
        img = cv2.imread(ROOT_DIR + '/Data/classroom_images/unmarked_class.jpg')
        self.Group = Group(101, "algorithms", img)
        self.testobj = FaceMatcher(self.Group)

    def test_process(self):
        self.assertEqual(self.testobj.process(), 1)



if __name__ == '__main__':
    unittest.main()