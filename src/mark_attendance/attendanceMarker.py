import requests
import json

from src.mark_attendance.config import *
import mysql.connector

from datetime import datetime
import calendar


def getDate():
    datetime_object = datetime.now()
    month=datetime_object.month
    year=datetime_object.year
    date=datetime_object.day
    val=str(date)+"_"+str(month)+"_"+str(year)
    val=str(val)

    val_1=""+val
    return val_1

def getDatabaseConnection():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="Attendences"
    )
    return db_connection, db_connection.cursor()


class AttendanceMarker:

    
    def sendAttendance(self, roll_no, subject_code):
        data = {
            'subject_code' : subject_code,
            'students' : roll_no
        }
        try:
            requests.post(url = DESTINATION_ADDRESS, json = json.dump(data))
        except Exception as e:
            print("Error : {}".format(e))

    def mark_present(self, students,subject_code):
        roll_no=[]
        for val in students:
            roll_no.append(val.getRollNo())
        
        db_connection, cursor = getDatabaseConnection()
        date = getDate()
        # print(data)
        for student in roll_no:
            #sql="UPDATE student5 SET "+date+"='present' where subject_code = "+str(subject_code)+" and student_id="+str(student)
            sql = "INSERT INTO attendence (date, subject_code, student_id) VALUES (%s ,%s, %s)" 
            val = (date,subject_code,student)
            cursor.execute(sql, val)
            db_connection.commit()
        
        # self.sendAttendance(roll_no, subject_code)
        return 1