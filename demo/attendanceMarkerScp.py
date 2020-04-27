import os
import time
from demo.config import *
from datetime import datetime

class AttendanceMarkerScp:

    def __init__(self):
        self.roll_no=[]

    def parseDateTime(self,datetimestr):
        s=''
        for i in datetimestr:
            if i=='/':
                s=s+'_'
            else:
                s=s+i
        return s
    def sendAttendance(self,stu_info, subject_code):
        #first we have to create a file. name it temp.
        f=open('tempfile','w')
        f.writelines(str(subject_code)+'\n')
        for i in stu_info:
            roll_no=i[0]
            name=i[1]
            f.writelines(str(roll_no)+' '+name+'\n')
        f.close()
        now = datetime.now()
        date_time = self.parseDateTime(now.strftime("%m/%d/%Y,%H:%M:%S"))
        remoteFilePath='~/a_'+str(subject_code)+'_'+date_time
        #now we have to send the file to the common node.
        print('the remotefile is ',remoteFilePath)
        os.system('scp tempfile nabhiraj@localhost:'+remoteFilePath)
        time.sleep(2)
        os.remove('tempfile')
        
        

    def mark_present(self, students,subject_code):
        info=[]
        for val in students:
            roll_no=val.getRollNo()
            name=val.getName()
            info.append((roll_no,name))
        self.roll_no = roll_no
        self.sendAttendance(info, subject_code)