import unittest
from src.mark_attendance.faceMatcher import FaceMatcher
from src.entities.group import Group
import cv2


class TestFaceMatcher(unittest.TestCase):
    def setUp(self):
        img = cv2.imread('../classroom_images/unmarked_class.jpg')
        self.Group = Group(101, "algorithms", img)
        self.testobj = FaceMatcher(self.Group)

    def test_process(self):
        self.assertEqual(self.testobj.process(), 1)



if __name__ == '__main__':
    unittest.main()