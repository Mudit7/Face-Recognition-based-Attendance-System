# Face-Recognition-based-Attendance-System

## Registration

To run the face and information extraction model. Please follow the installing intructions in src/registration/README.md 

We have also implemented the Web interface using Flask and Mysql database (conifg accodringly).
### To run the Web Interface
Enter the command where xxxx denotes the port number by default it will run on 8080 port.
```
python3 index.py xxxx
```
### Output of Model
Will store the extracted information and faces in /static folder in orde to use this inforamtion for attendence.
1. /static/json  -> Will store the Json file corresponding to the uploaded ID CARD.
2. /static/faces -> Will store the face extracted from the uploaded ID CARD.
3. /static/cards -> Will store the uploaded ID CARD.
NOTE:: In /static name of files has been automated i.e you can upload image with any name it will be saved automatically to the corresponding roll number on card.
4. app.sql is a Database, currently it has only Students Table and Database name is Attendences. Please add Table corresponding to each course.

