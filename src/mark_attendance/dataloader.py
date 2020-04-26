from src.entities.student import Student
from src.entities.subject import Subject
import cv2
#this is temporary dataloader just created for testing.
class DataLoader:
    # mysub=None
    # s_babita=None
    # s_sheldon=None
    # s_ram=None
    def __init__(self):
        #creating sudents.
        loc_dir='/Users/mudit/Desktop/SE_Proj/Face-Recognition-based-Attendance-System/students_images/'
        self.s_babita=Student(1,
                              'babita',
                              cv2.imread(loc_dir+'babita.jpg'))

        self.s_sheldon=Student(2,
                               'sheldon',
                               cv2.imread(loc_dir+'sheldon.jpg'))

        self.s_ram=Student(3,
                           'ram',
                           cv2.imread(loc_dir+'ram.jpg'))
        #now we will make he list.
        self.s_gita=Student(4,
                            'gita',
                            cv2.imread(loc_dir+'gita.jpg'))
        self.s_syam=Student(5,
                            'syam',
                            cv2.imread(loc_dir+'syam.jpg'))
        self.s_peter=Student(6,
                             'peter',
                             cv2.imread(loc_dir+'peter.jpg'))
        l1=[self.s_babita,self.s_sheldon,self.s_ram]
        l2=[self.s_babita,self.s_sheldon,self.s_ram,self.s_gita,self.s_syam]
        self.mysub=[Subject(101,'algorithms',l2),Subject(102,'toc',l1),Subject(103,'os',l1),Subject(104,'DMA',l2)]

    def getSubject(self,subCode):
        # print("subject code",subCode)
        for i in self.mysub:
            if i.getSubjectCode()==subCode:
                print("subject name",i.getSubjectName())
                return i