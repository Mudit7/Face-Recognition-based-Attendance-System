import pip
pip.main(['install','mysql-connector-python-rf'])
import mysql.connector
from datetime import datetime
import calendar
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
cursor = db_connection.cursor()
#query = "ALTER TABLE student1 ADD {} VARCHAR(500)".format(val)
#query = "ALTER TABLE student1 ADD %s VARCHAR(500)"%(val)
query="ALTER TABLE student5 ADD COLUMN "+str(val_1)+" VARCHAR(100) DEFAULT 'absent'"
cursor.execute(query)
#query_1="ALTER TABLE student2 ALTER "+str(val_1)+" SET DEFAULT 0"
#cursor.execute(query_1)