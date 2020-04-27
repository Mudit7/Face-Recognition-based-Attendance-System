import requests
import json

from config import *

class AttendanceMarker:

    def __init__(self):
        self.roll_no=[]

    def sendAttendance(self, roll_no, subject_code):
        data = {
            'subject_code' : subject_code,
            'students' : roll_no
        }
        try:
            requests.post(url = DESTINATION_ADDRESS, data = json.dumps(data))
        except Exception as e:
            print("Error : {}".format(e))

    def mark_present(self, students,subject_code):
        roll_no=[]
        for val in students:
            roll_no.append(val.getRollNo())
        self.roll_no = roll_no
        self.sendAttendance(roll_no, subject_code)