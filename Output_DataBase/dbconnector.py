#import mysql.connector
#import MySQLdb
import pip
pip.main(['install','mysql-connector-python-rf'])
import mysql.connector
from datetime import date
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Hardcore@007",
  database="mydatabase")
print(db_connection)
#curr_date=mycursor.execute(SELECT CURDATE());
today = date.today()
mycursor = db_connection.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")
#mycursor.execute("SHOW DATABASES")
mycursor.execute("CREATE TABLE student5 (student_id INT, name VARCHAR(255),subject_code INT)")

#for x in mycursor:
#  print(x)