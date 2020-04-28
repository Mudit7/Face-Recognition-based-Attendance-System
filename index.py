import os, json
from sys import argv
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
import time
from random import random
from flask_mysqldb import MySQL
import MySQLdb

from src.entities.group import Group
from src.mark_attendance.faceMatcher import FaceMatcher
import cv2
from datetime import datetime



BASE_FOLDER = 'src/registration/'
UPLOAD_FOLDER = BASE_FOLDER + 'Source'
ATTEND_FOLDER =  'static/Class_photo'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Attendences'
mysql = MySQL(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ATTEND_FOLDER'] = ATTEND_FOLDER

def getDate():
    datetime_object = datetime.now()
    month=datetime_object.month
    year=datetime_object.year
    date=datetime_object.day
    val=str(date)+"_"+str(month)+"_"+str(year)
    val=str(val)

    val_1=""+val
    return val_1

def allowed_file(filename):
    return filename[-3:].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('home.html')

    #return redirect(url_for('upload_file'))

@app.route('/uploadIdCard', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        # If post request has file in it
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                print ('**found file', file.filename)
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                time.sleep(random() * .1 * 60)
                Flask_dir = os.getcwd()
                ### Change Directory to ID card Folder of run.sh 
                os.chdir(BASE_FOLDER)
                os.system('./run.sh')
                #print(os.getcwd())
                f = open("Output/json/" + "res_" + filename.split('.')[0] + ".json", "r")
                a = f.read()
                y = json.loads(a) 
                roll_number = y['roll_no']

                ## Back to normal directory
                os.chdir(Flask_dir)
                #print(os.getcwd())
                return redirect(url_for('show_details', filename=roll_number))             
    return render_template('index.html')

@app.route('/attendance', methods=['GET', 'POST'])
def upload_attendace():
    if request.method == 'POST':
        
        # If post request has file in it
        if 'file' in request.files:
            file = request.files['file']
            if file and allowed_file(file.filename):
                print ('**found file', file.filename)
                classid = request.form['text']
                classname = request.form['text1']
                classid = classid
                #remove previous photo
                if os.path.exists(os.path.join(app.config['ATTEND_FOLDER'], classid)):
                    os.remove(os.path.join(app.config['ATTEND_FOLDER'], classid))
                    pp = os.path.join("static/extracted_faces_from_class", classid)
                    os.system("rm -rf " + pp)
                    os.system("mkdir " + pp)
                filename = secure_filename(file.filename)
                media_path = os.path.join(app.config['ATTEND_FOLDER'], classid)
                file.save(os.path.join(app.config['ATTEND_FOLDER'], classid))
                time.sleep(random() * .1 * 60)

        subject_code = int(classid)
        subject_name = classname
        img=cv2.imread(media_path, cv2.COLOR_BGR2RGB)
        grp=Group(subject_code, subject_name, img)
        Fmatcher=FaceMatcher(grp)
        Fmatcher.process()
        return redirect(url_for('show_class_details', filename = classid))              
    return render_template('indexat.html')

@app.route('/checkAttendance',methods=['GET', 'POST'])
def Check_attendence():
    if request.method == "POST":
        username = request.form["rollno"]
        classid = request.form["classid"]
        mycursor = mysql.connection.cursor()
        mycursor.execute("Show columns FROM attendence")
        headers = mycursor.fetchall()
        #print(headers)
        mycursor.execute("SELECT distinct * FROM attendence where student_id='" + username + "'" + "and subject_code='" + classid + "'")
        myresult = mycursor.fetchall()
        #print(myresult)
        if len(myresult) == 0:
            return render_template('index.html')

        return render_template('studinfo.html',items=myresult,item1=headers)
                    
    return render_template('checkAttend.html')



@app.route('/showDetails/<filename>')
def show_details(filename):
    return render_template('show.html', path=BASE_FOLDER, id=filename)


@app.route('/showClassDetails/<filename>')
def show_class_details(filename):
    a = os.listdir("static/extracted_faces_from_class/" + filename + "")
    size = len(a)
    cur = mysql.connection.cursor()
    sql = 'SELECT Students.name, Students.roll_no, classes.class_name FROM Students INNER JOIN classes ON Students.roll_no=classes.student_id and classes.class_id = ' +  filename
    cur.execute(sql)
    myresult = cur.fetchall()
    
    date = getDate()
    present = []
    sql = 'select DISTINCTROW student_id from attendence where date = "' + date + '" and subject_code = '+ filename
    # print (sql)
    cur.execute(sql)
    myresult1 = cur.fetchall()
    for x in myresult1:
        present.append(x[0])
    # print(present)
    classs = ""
    data = []
    DD = {}
    for x in myresult:
        st = {}
        st['name'] = x[0]
        st['roll_no'] = x[1]
        st['class'] = x[2]
        classs = x[2].upper()
        st['attend'] = "Absent"
        if x[1] in present:
            st['attend'] = "Present"
        data.append(st)
    # print(data)
    DD['attendence'] = data
    with open('static/finalJson/'+ filename +'.json', 'w', encoding='utf-8') as outfile:
        str_ = json.dumps(DD)
        outfile.write(str_)
    return render_template('showClass.html', Faces=size,classs=classs ,id=filename, json = json.dumps(data))


@app.route('/update/<id>')
def updatedatabase(id):
    f = open("static/json/" + id + ".json", "r")
    a = f.read()
    y = json.loads(a)
    cur = mysql.connection.cursor()
    try:
        try:
            cur.execute("DELETE FROM Students WHERE roll_no = 20171189")
            mysql.connection.commit()
            # NB : you won't get an IntegrityError when reading
        except :
            print('NO Entry')
        try:
            cur.execute("INSERT INTO Students(collegeName, name, roll_no, email, branch, mobile, validity) VALUES (%s, %s, %s, %s, %s, %s, %s)", (y['college'], y['name'], y['roll_no'], y['emails'], y['branch'], y['mobile'], y['valid']))
            mysql.connection.commit()
            # NB : you won't get an IntegrityError when reading
        except :
            print('Please Try Again!!')
            return render_template('fail.html')


    finally:
        cur.close()
    return render_template('success.html')


if __name__ == '__main__':
    if len(argv) == 2:
        port = int(argv[1])
        print (f"Application is ready and listening to port {port}")
        app.run(host='localhost', port=port, debug=True)
        
    else:
        app.run(host='localhost', port=8080, debug=True)
        print (f"Application is ready and listening to port {port}")

