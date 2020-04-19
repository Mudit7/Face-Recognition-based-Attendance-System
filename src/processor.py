# !pip install keras-facenet

import numpy as np
from keras_facenet import FaceNet

from attendanceMarker import AttendanceMarker
from bufferManager import BufferManager
from subject import Subject
from student import Student
from face_extract import api as Extractor

class Processor:
  studentList = []
  encodedStudentFaces = []
  encodedExtractedFaces = []
  presentStudents = []
  studentImages = []

  def __init__(self,grp):
    subjectCode = grp.getSubjectCode()
    BM = BufferManager()
    subject = BM.getSubject(subjectCode)
    studentList = subject.getStudentList()
    attendance_arr = [0]*len(studentList)
    groupImage= grp.getGroupImage()
    extractedFaces = Extractor.cropFaces(groupImage)
    #Encode using the FACENET
    for student in studentList:
      studentImages.append(student.getImage())

    embedder = FaceNet()
    encodedStudentFaces = embedder.embeddings(studentImages)
    encodedExtractedFaces = embedder.embeddings(extractedFaces)

  def process(self):
    for encodedVec in encodedExtractedFaces:
      student = getBestMatchStudent(encodedVec)
      presentStudents.append(student)

    AM = AttendanceMarker()
    AM.markPresent(presentStudents)

  def getBestMatchStudent(self,extractedVec):
    diffVec = []
    for studentVec in encodedStudentFaces:
      dist = np.linalg.norm(studentVec - extractedVec)
      diffVec.append(dist)
    minIndex = diffVec.index(min(diffVec))
    return studentList[minIndex]