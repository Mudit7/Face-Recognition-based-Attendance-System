from src.entities.student import Student
from src.entities.subject import Subject
import cv2
from root_config import ROOT_DIR
#this is temporary dataloader just created for testing.
class DataLoader:
    # mysub=None
    # s_babita=None
    # s_sheldon=None
    # s_ram=None
    def __init__(self):
        #creating sudents.
        loc_dir=ROOT_DIR+'/students_images/'
        print('the directory is ',loc_dir)
        self.s_babita=Student(1,
                              'babita',
                              cv2.imread(loc_dir+'babita.jpg',cv2.COLOR_BGR2RGB))

        self.s_sheldon=Student(2,
                               'sheldon',
                               cv2.imread(loc_dir+'sheldon.jpg',cv2.COLOR_BGR2RGB))

        self.s_ram=Student(3,
                           'ram',
                           cv2.imread(loc_dir+'ram.jpg',cv2.COLOR_BGR2RGB))
        #now we will make he list.
        self.s_gita=Student(4,
                            'gita',
                            cv2.imread(loc_dir+'gita.jpg',cv2.COLOR_BGR2RGB))
        self.s_syam=Student(5,
                            'syam',
                            cv2.imread(loc_dir+'syam.jpg',cv2.COLOR_BGR2RGB))
        self.s_peter=Student(6,
                             'peter',
                             cv2.imread(loc_dir+'peter.jpg',cv2.COLOR_BGR2RGB))
        l1=[self.s_babita,self.s_sheldon,self.s_ram]
        l2=[self.s_babita,self.s_sheldon,self.s_ram,self.s_gita,self.s_syam]
        self.mysub=[Subject(101,'algorithms',l2),Subject(102,'toc',l1),Subject(103,'os',l1),Subject(104,'DMA',l2)]

    def getSubject(self,subCode):
        print('query of subject from data loader')
        for i in self.mysub:
            if i.getSubjectCode()==subCode:
                return i