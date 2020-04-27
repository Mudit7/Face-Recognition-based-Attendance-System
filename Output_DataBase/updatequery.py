import pip
pip.main(['install','mysql-connector-python-rf'])
import mysql.connector

from datetime import datetime
import calendar

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

def getDate():
	datetime_object = datetime.now()
	month=datetime_object.month
	year=datetime_object.year
	date=datetime_object.day
	val=str(date)+"_"+str(month)+"_"+str(year)
	val=str(val)

	val_1=""+val

def getDatabaseConnection():
	db_connection = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="Hardcore@007",
		database="mydatabase"
	)
	return db_connection, db_connection.cursor()


@app.route('/', methods = ['POST'])
def update_table():
	if request.method == 'POST':
		data = request.get_json()
		subject_code = data['subject_code']
		present_student_list = data['studentList']
		
		db_connection, cursor = getDatabaseConnection()

		date = getDate()

		for student in present_student_list:
			sql="UPDATE student5 SET "+date+"='present' where subject_code = "+str(subject_code)+" and student_id="+str(student)
			cursor.execute(sql)
			db_connection.commit()

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=8081)
