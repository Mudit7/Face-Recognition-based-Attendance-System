from tkinter import Label
from tkinter import StringVar
import tkinter
from tkinter import RAISED
from tkinter import LEFT 
from tkinter import Entry
from tkinter import RIGHT
from tkinter import filedialog

import src.upload_media as upload_media

def selectFile():
    top.filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    path_label_var.set(top.filename)

def startProcess():
    file_path=top.filename
    sub_code=sub_code_entry.get()
    upload_media.send_media(sub_code, file_path)

top=tkinter.Tk()
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
path_button.pack()
path_label.pack()
B.pack()
top.mainloop()