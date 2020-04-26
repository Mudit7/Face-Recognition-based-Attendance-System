import pip
pip.main(['install','mysql-connector-python-rf'])
import mysql.connector
from datetime import datetime
import calendar
def update_table(l,code):
    db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Hardcore@007",
            database="mydatabase")
    #print(db_connection)
    datetime_object = datetime.now()
    month=datetime_object.month
    year=datetime_object.year
    date=datetime_object.day
    val=str(date)+"_"+str(month)+"_"+str(year)
    val=str(val)
    #print('date is:->'+val)
    val_1=""+val
    #print(val_1)
    cursor = db_connection.cursor()
    for val in l:
        #sql = "UPDATE student2 SET "+val_1+"='absent' WHERE student_id ="+str(val[2])+" AND subject_code="+str(val[3])
        #sql = "UPDATE student2 SET "+val_1+"='absent' WHERE student2.student_id ="+str(val[2])+" and student2.subject_code="+str(val[3])
        #sql="UPDATE student2 SET "+val_1+"='absent' where subject_code='CS471' and student_id=2019201059"
        sql="UPDATE student5 SET "+val_1+"='present' where subject_code = "+str(code)+" and student_id="+str(val[2])
        cursor.execute(sql)
        #cursor.execut
        db_connection.commit()
        print('yes')

l=[('vikram',9,2019201059,123),('rish',4,2019201074,123)]
code=123
update_table(l,code)

