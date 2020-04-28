from src.entities.student import Student
from src.entities.subject import Subject
import cv2
from root_config import ROOT_DIR
import os, json
import mysql.connector

#this is temporary dataloader just created for testing.
def getDatabaseConnection():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="Attendences"
    )
    return db_connection, db_connection.cursor()

class DataLoader:
 
    def __init__(self):
        #creating sudents.
        self.allStudents = []
        loc_dir=ROOT_DIR+'/static/'
        for filename in os.listdir(loc_dir + 'json'):
            if filename.endswith(".json"): 
                f = open(loc_dir + 'json/' + filename)
                data = json.load(f)
                name = data['name'] 
                t_name = 's_' + name.lower()
                self.allStudents.append(t_name)
            else:
                continue

        i = 0
        for filename in os.listdir(loc_dir + 'json'):
            if filename.endswith(".json"): 
                f = open(loc_dir + 'json/' + filename)
                data = json.load(f)
                name = data['name'] 
                t_name = 's_' + name.lower() 
                self.allStudents[i] = Student(data['roll_no'],name, 
                  cv2.imread(loc_dir+'faces/'+data['roll_no'] + '.jpg'))
                i = i + 1
            else:
                continue
        # print(self.allStudents)

        self.mysub = []
        lists=[]
        db_connection, cursor = getDatabaseConnection() 
        cursor.execute("select distinct class_id,class_name from classes")
        myresult = cursor.fetchall()
        for x in myresult:
          print(x[0])
          l = []
          cursor.execute("select * from classes where class_id =" + str(x[0]))
          myresult1 = cursor.fetchall()
          for y in myresult1:
            for student in self.allStudents:
              if y[2] == student.studentRollNo: 
                l.append(student)
                self.mysub.append(Subject(int(x[0]),x[1],l))

    def getSubject(self,subCode):
        for i in self.mysub:
            if i.getSubjectCode()==subCode:
                return i