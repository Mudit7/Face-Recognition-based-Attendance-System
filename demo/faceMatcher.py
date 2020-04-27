# !pip install keras-facenet

import numpy as np
from keras_facenet import FaceNet
from src.face_extract import api as Extractor
from demo.attendanceMarkerScp import AttendanceMarkerScp
from demo.bufferManeger import BufferManeger
from src.entities.student import Student
from demo.buffer_config import *
from demo.bufferArg import BufferArg
import cv2
from tqdm import tqdm
threshold = 0.15

class FaceMatcher:


    def __init__(self, grp):
        self.student_list = []
        self.encoded_student_faces = []
        self.encoded_extracted_faces = []
        self.present_students = []
        self.student_images = []
        self.subject_code = grp.getSubjectCode()
        bmArg = BufferArg()
        bmArg.setPath(BUFFER_DIR)
        bmArg.setExpirationTime(EXPIRE_DAYS)
        bmArg.setNumOfSub(NO_OF_SUB)
        bm = BufferManeger(bmArg)
        cur_subject = bm.getSubject(self.subject_code)
        self.student_list = cur_subject.getStudentList()

        group_image = grp.getGroupImage()
        extracted_faces = Extractor.cropFaces(group_image)
        # *****************************
        # Encode using the FACENET


        # for testing************
        #
        # self.student_list.append(Student(1,"syam",cv2.imread('../students_images/syam.jpg')))
        # self.student_list.append(Student(2,"sheldon",cv2.imread('../students_images/sheldon.jpg')))
        # self.student_list.append(Student(3,"babita",cv2.imread('../students_images/babita.jpg')))
        # self.student_list.append(Student(4,"gita",cv2.imread('../students_images/gita.jpg')))
        # self.student_list.append(Student(5,"ram",cv2.imread('../students_images/ram.jpg')))

        #*****************************
        for student in self.student_list:
            self.student_images.append(student.getImage())

        embedder = FaceNet()
        self.student_images = np.array(self.student_images)
        extracted_faces = np.array(extracted_faces)
        self.encoded_student_faces = embedder.embeddings(self.student_images)
        self.encoded_extracted_faces = embedder.embeddings(extracted_faces)

    def process(self):
        for encodedVec in self.encoded_extracted_faces:
            student = self.get_best_match_student(encodedVec)
            if student is not None:
                self.present_students.append(student)

        am = AttendanceMarkerScp()
        success = am.mark_present(self.present_students,self.subject_code)
        return success

    def get_best_match_student(self, extractedVec):
        diff_vec = []
        for studentVec in self.encoded_student_faces:
            dist = np.linalg.norm(studentVec - extractedVec)
            diff_vec.append(dist)
        min_index = diff_vec.index(min(diff_vec))
        print(diff_vec[min_index])
        if diff_vec[min_index] > threshold:    #if a good match
            return self.student_list[min_index]
        else:
            return None
