import os, json
from sys import argv
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename
import time
from random import random
from flask_mysqldb import MySQL
import MySQLdb

BASE_FOLDER = 'src/registration/'
UPLOAD_FOLDER = BASE_FOLDER + 'Source'
ATTEND_FOLDER = BASE_FOLDER + 'Class_photo'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Attendences'
mysql = MySQL(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ATTEND_FOLDER'] = ATTEND_FOLDER


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
                classid = classid + "_" + time.ctime()
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['ATTEND_FOLDER'], classid))
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
    return render_template('indexat.html')


@app.route('/showDetails/<filename>')
def show_details(filename):
    return render_template('show.html', path=BASE_FOLDER, id=filename)


@app.route('/update/<id>')
def updatedatabase(id):
    f = open("static/json/" + id + ".json", "r")
    a = f.read()
    y = json.loads(a)
    cur = mysql.connection.cursor()
    try:
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

