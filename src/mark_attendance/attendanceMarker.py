import requests
import json

from src.mark_attendance.config import *

class AttendanceMarker:

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
        self.sendAttendance(roll_no, subject_code)
        return 1