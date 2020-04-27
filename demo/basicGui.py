from tkinter import Label
from tkinter import StringVar
import tkinter
from tkinter import RAISED
from tkinter import Entry
from tkinter import filedialog
from src.entities.group import Group
from demo.faceMatcher import FaceMatcher
import cv2
import threading

def selectFile():
    top.filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    path_label_var.set(top.filename)
    
def startProcessThread(sub_code,sub_name,path):
    print('starting the thread')
    print('name is ',sub_name)
    print('sub code is ',sub_code)
    print('the path is ',path)
    img=cv2.imread(path,cv2.COLOR_BGR2RGB)
    print('the imag is ',img)
    grp=Group(sub_code,sub_name,img)
    print('calling facemather object')
    Fmatcher=FaceMatcher(grp)
    print('startint the processing')
    Fmatcher.process()
    
def startProcess():
    #this thing has to be done in a new thread.
    file_path=top.filename
    sub_code=sub_code_entry.get()
    sub_name=sub_name_entry.get()
    print('calling the thread')
    t=threading.Thread(target = startProcessThread, args = (int(sub_code),sub_name,file_path))
    t.start()
    
top=tkinter.Tk()

print('top created')

B=tkinter.Button(top,text='start Process',command=startProcess)
sub_code_var=StringVar()
sub_code_label=Label(top,textvariable=sub_code_var,relief=RAISED)
sub_code_var.set('enter the subject code')
sub_code_label.pack()
sub_code_entry=Entry(top,bd=5)
sub_code_entry.pack()
path_label_var=StringVar()
path_label=Label(top,textvariable=path_label_var,relief=RAISED)
path_label_var.set('None')
path_button=tkinter.Button(top,text='select image',command=selectFile)
sub_name_var=StringVar()
sub_name_label=Label(top,textvariable=sub_name_var,relief=RAISED)
print('enter the subject name')
sub_name_var.set('enter the subject name')
sub_name_label.pack()
print('entry 1')
sub_name_entry=Entry()
print('entry 2')
sub_name_entry.pack()
path_button.pack()
path_label.pack()
B.pack()
print('everything packed')
top.mainloop()