# !pip install keras-facenet

import numpy as np
from keras_facenet import FaceNet
from src.face_extract import api as Extractor
from src.mark_attendance.attendanceMarker import AttendanceMarker
from src.mark_attendance.bufferManager import BufferManager
from src.entities.student import Student
import cv2


class FaceMatcher:


    def __init__(self, grp):
        self.student_list = []
        self.encoded_student_faces = []
        self.encoded_extracted_faces = []
        self.present_students = []
        self.student_images = []
        subject_code = grp.getSubjectCode()
        bm = BufferManager('path')
        cur_subject = bm.getSubject(subject_code)
        self.student_list = []

        group_image = grp.getGroupImage()
        extracted_faces = Extractor.cropFaces(group_image)
        # *****************************
        # Encode using the FACENET


        # for testing************

        self.student_list.append(Student(1,"syam",cv2.imread('../students_images/syam.jpg')))
        self.student_list.append(Student(2,"sheldon",cv2.imread('../students_images/sheldon.jpg')))
        self.student_list.append(Student(3,"babita",cv2.imread('../students_images/babita.jpg')))
        self.student_list.append(Student(4,"gita",cv2.imread('../students_images/gita.jpg')))
        self.student_list.append(Student(5,"ram",cv2.imread('../students_images/ram.jpg')))

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
            self.present_students.append(student)

        am = AttendanceMarker()
        success = am.mark_present(self.present_students)
        return success

    def get_best_match_student(self, extractedVec):
        diff_vec = []
        for studentVec in self.encoded_student_faces:
            dist = np.linalg.norm(studentVec - extractedVec)
            diff_vec.append(dist)
        min_index = diff_vec.index(min(diff_vec))
        return self.student_list[min_index]
