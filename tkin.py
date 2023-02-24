from datetime import datetime
import glob
import re
from PIL import ImageTk, Image
import tkinter
from PIL import Image
from conect_to_DB import mycursor
from conect_to_DB import myconn
import tkinter as tk
from tkinter import *
from student import Student
from day import *
from attendance import takeAttendance
from section import Sction
from sectionRegistration import Student_to_section
import pickle
import cv2
from staff import Staff
from course import Course
from new_class import Nclass
from teach import Teach
from report import *
from sys import path
import os
from tkinter import messagebox
from PIL import Image
import numpy as np
from studentphotos import StudentPhoto


global face_cascade2,face_cascade
face_cascade = cv2.CascadeClassifier(
    'cascades/data/haarcascade_profileface.xml')
face_cascade2 = cv2.CascadeClassifier(
    'cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")
# ==========================create new folder for photos==================
def checkStudentinfoEntry():
    if len(student_id.get()) != 10 or not student_id.get().isdigit():
        tkinter.messagebox.showinfo(title=None, message="student id must contain 10 numbers ")
        student_id.delete(0,'end')
    elif len(student_first_name.get()) > 45 or len(student_first_name.get())==0:
        student_first_name.delete(0,'end')
        tkinter.messagebox.showinfo(title=None, message="student first name  more than 45 or 0 characters ")
     
    elif len(student_last_name.get()) > 45 or len(student_last_name.get())==0:
        tkinter.messagebox.showinfo(title=None, message="student last name  more than 45 or 0 characters ")
        student_last_name.delete(0,'end')
        
    elif len(student_email.get()) > 45 or len(student_email.get())==0:
        tkinter.messagebox.showinfo(title=None, message="student email   more than 200 or 0 characters ")
        student_email.delete(0,'end')
        student_id.delete(0,'end')
    else:
   
        print(student_id.get(),student_first_name.get(),student_last_name.get(),student_email.get())
        newStudent = Student(student_id.get(),student_first_name.get(),student_last_name.get(),student_email.get())
        checkId=newStudent.check() #check if the student id already exist in database
        if checkId==True: #check if the student id already exist in database
         tkinter.messagebox.showinfo(title=None, message="there is another student with the same ID in the database ")
        else:

         newStudent.insert()
         tkinter.messagebox.showinfo(title=None, message="student information inserted to database ")
            
        dir()
        
def dir():
    global parent_dir
    parent_dir = r"C:\Users\amera\OneDrive\Desktop\attendance system based on face recognition\My_Dataset"
    global directory
    directory = student_id.get()
    global path
    path = os.path.join(parent_dir, directory)
    if  os.path.exists(path)  :#if the file exist  send maseges
      tkinter.messagebox.showinfo(title=None, message="the folder already exists")
    elif not os.path.exists(path):
     os.mkdir(path) 
     myphotp()
    elif os.listdir(path) == 0 :#if the file exist but there is no photos in the file call myphotp
    
     myphotp() # Take pictures from the cam 

        
def submitANDinsert():#submit  to add the student information with photo in database
    directory = student_id.get()
    parent_dir = r"C:\Users\amera\OneDrive\Desktop\attendance system based on face recognition\My_Dataset"
    paths = os.path.join(parent_dir, directory)
    print(paths)
    newStudent = StudentPhoto(int(directory),  str(paths))
    checkId=newStudent.check()
    checkId2=newStudent.check2()
    if len(student_id.get()) != 10 or not student_id.get().isdigit():
        tkinter.messagebox.showinfo(title=None, message="student id must contain 10 numbers ")
        student_id.delete(0,'end')
    elif not os.path.exists(paths):
        student_id.delete(0,'end')
        tkinter.messagebox.showinfo(title=None, message=" there is no directory for this student in dataset please complete student information than click on take photo ")
        #check if the student id already exist in database
     #check if the student id already exist in database
    elif checkId==True and checkId2==True:
            tkinter.messagebox.showinfo(title=None, message="there is another student directory with the same id in database if this student ID is correct than student information already exists in database ")
          
    elif checkId2==True and checkId==False and os.path.exists(paths):
         newStudent.insert2()
         tkinter.messagebox.showinfo(title=None, message="the directory inserted into the database ")
    elif checkId==False  and  os.path.exists(paths) and checkId2==False:
        tkinter.messagebox.showinfo(title=None, message="the directory is exist but there is no information for this student in the database please compleat the student information than click submit  ")
        

def myphotp():

 cap = cv2.VideoCapture(0)
 sampleNum=0

 while (True):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.1, 4)
  facess = face_cascade2.detectMultiScale(gray, 1.4, 5)
  for (x, y, w, h) in faces:
      roi_gray = gray[y:y+h, x:x+w]
      cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
      cv2.putText(frame, 'Number of photos: ' + str(sampleNum), (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
      cv2.imwrite(os.path.join(path, str(sampleNum)+'.png'),roi_gray)
      sampleNum+=1
      cv2.imshow('frame', frame)
      print(sampleNum)
  
  
  for (xi, yi, wi, hi) in facess:  
      roi_gray = gray[yi:yi+hi, xi:xi+wi]
      cv2.rectangle(frame, (xi, yi), (xi+wi, yi+hi), (255, 0, 0), 2)
      cv2.putText(frame, 'Number of photos: ' + str(sampleNum), (x, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
      cv2.imwrite(os.path.join(path, str(sampleNum)+'.png'),roi_gray)
      sampleNum+=1
      cv2.imshow('frame', frame)

  if cv2.waitKey(100) & 0xFF == ord('q'):
       tkinter.messagebox.showinfo(title=None, message="please make sure to training the module")
       break
  elif sampleNum > 100:
       tkinter.messagebox.showinfo(title=None, message="please make sure to training the module")
       break
 cap.release()
 cv2.destroyAllWindows()
  

# =========window for adding new student ===========


def TopNStudent():
    top = Toplevel(root)
    top.geometry('300x300')
    global student_id_lsbel
    student_id_lsbel = Label(top, text="Enter student ID:")
    global student_id
    student_id = tk.Entry(top, width=20,)
    student_first_name_lsbel = Label(top, text="Enter student first name:")
    global student_first_name
    student_first_name = tk.Entry(top, width=20,)
    student_last_name_lsbel = Label(top, text="Enter student last name:")
    global student_last_name
    student_last_name = tk.Entry(top, width=20,)
    student_email_lsbel = Label(top, text="Enter tudent email:")
    global student_email
    student_email = tk.Entry(top, width=20,)
    button_submit = Button(
        top, text="Take Photos", command=checkStudentinfoEntry, width=15, height=3, fg='white', bg='green')
    button_take_photo = Button(
        top, text="submit", command=submitANDinsert, width=15, height=3, fg='white', bg='green')

    student_id_lsbel.pack()
    student_id.pack()
    student_first_name_lsbel.pack()
    student_first_name.pack()
    student_last_name_lsbel.pack()
    student_last_name.pack()
    student_email_lsbel.pack()
    student_email.pack()
    button_submit.pack()
    button_take_photo.pack()
    
# ---------------------------staff windoe--------------------------------------
# =================Staff function=========================


def insertnewstt():
    if len(staffid.get()) !=10  or not staffid.get().isdigit():
        tkinter.messagebox.showinfo(title=None, message="staff id must contain  10 numbers ")
    elif len(staffFname.get()) > 45 or len(staffFname.get())==0:
        tkinter.messagebox.showinfo(title=None, message="staff first name  more than 45 or 0 characters ")
    elif len(staffLname.get()) > 45 or len(staffLname.get())==0:
        tkinter.messagebox.showinfo(title=None, message="staff last name  more than 45 or 0 characters ")
    elif len(staffEmail.get()) > 50 or len(staffLname.get())==0:
        tkinter.messagebox.showinfo(title=None, message="staff Email   more than 45 or 0 characters ")
    else:
     newstaff = Staff(staffFname.get(), staffLname.get(),staffEmail.get(), staffid.get())
     if newstaff.check()==True:
        tkinter.messagebox.showinfo(title=None, message="there is another staff has the same id ")
     else:
        newstaff.insert()
        tkinter.messagebox.showinfo(title=None, message="staff information inserted into database ")
# ===============taking photo function=============


def topstaff():
    top = Toplevel(root)
    top.geometry('300x300')
    staffid_id_label = Label(top, text="ID:")
    global staffid
    staffid = tk.Entry(top, width=20,)

    staff_first_name_label = Label(top, text="First Name:")
    global staffFname
    staffFname = tk.Entry(top, width=20,)
    staffLname_label = Label(top, text="Last Name:")
    global staffLname
    staffLname = tk.Entry(top, width=20,)
    stafft_email_lsbel = Label(top, text=" Email:")
    global staffEmail
    staffEmail = tk.Entry(top, width=20,)
    button_submit2 = Button(
        top, text="submit", command=insertnewstt, width=15, height=3, fg='white', bg='green')

    staffid_id_label.pack()
    staffid.pack()
    staff_first_name_label.pack()
    staffFname.pack()
    staffLname_label.pack()
    staffLname.pack()
    stafft_email_lsbel.pack()
    staffEmail.pack()
    button_submit2.pack()
    # ======================course window==============


def insertCourse():
   if len(courseId.get()) < 5  or len(courseId.get()) > 5:
        tkinter.messagebox.showinfo(title=None, message="Course id must contain of 5 characters  ")
   else:
     newCourse = Course(courseId.get(), courseName.get())
     if newCourse.check()==True:
          tkinter.messagebox.showinfo(title=None, message="there is another course withe the same id ")
     else:
      newCourse.insert()
      tkinter.messagebox.showinfo(title=None, message="the course inserted into database ")


def tech():
    newCourse = Course(courseId.get(), courseName.get())
    teachh = Teach(sel7.get(), courseId.get())
    
    if  sel7.get() == 0:
        tkinter.messagebox.showinfo(title=None, message="you must add staff id  ")
    elif newCourse.check()==False or len(courseId.get()) ==0 or len(courseName.get())==0:
         tkinter.messagebox.showinfo(title=None, message="The course ID and name you have entered do not match any existing course in the database, please double check the information and try again")
    else:     
        if teachh.check()==True:
           tkinter.messagebox.showinfo(title=None, message=" this staff already teach this course  ")
        else:
            tkinter.messagebox.showinfo(title=None, message=" you have entered  \\ staff id :"+str(sel7.get())+" Teach this "+" course name: "+str(courseName.get())+"  course id "+str( courseId.get()))
            teachh.insert()


def Topcourse():
    top = Toplevel(root)
    top.geometry('300x300')
    course_id_label = Label(top, text="course ID:")
    global courseId
    courseId = tk.Entry(top, width=20,)

    course_name_label = Label(top, text="course name:")
    global courseName
    courseName = tk.Entry(top, width=20,)
    button_submit3 = Button(
        top, text="Add", command=insertCourse, width=15, height=3, fg='white', bg='green')

    results = Staff.selectid()
    results_for_combobox = [result[0] for result in results]
    global sel7
    sel7 = IntVar()
    comboBox7 = ttk.Combobox(
        top, values=results_for_combobox, textvariable=sel7)

    staff_id_label = Label(
        top, text="Enter staff id how will teach this course:")

    button_submit4 = Button(
        top, text="Add staff", command=tech, width=15, height=3, fg='white', bg='green')

    course_id_label.pack()
    courseId.pack()
    course_name_label.pack()
    courseName.pack()
    button_submit3.pack()
    staff_id_label.pack()
    comboBox7.pack()
    comboBox7.state(['readonly'])
    button_submit4.pack()
# ============class window==============================


def insertClass():
    newclass = Nclass(classID.get(), classFloor.get())
    if newclass.check()==True:
        tkinter.messagebox.showinfo(title=None, message=" this Class already  exist in database  ")
    elif len(classID.get())<=4 or len( classFloor.get())<=8:
        tkinter.messagebox.showinfo(title=None, message=" wrong entry class id must be 5 characters and floor must be > 8 characters  ")
    else:
     newclass.insert()
     tkinter.messagebox.showinfo(title=None, message=" the class inserted into database  ")


def Topcclass():
    top = Toplevel(root)
    top.geometry('300x300')
    class_id_label = Label(top, text="Class_ID:")
    global classID
    classID = tk.Entry(top, width=20,)

    class_floor_label = Label(top, text="Floor:")
    global classFloor
    classFloor = tk.Entry(top, width=20,)
    button_submit4 = Button(
        top, text="submit", command=insertClass, width=15, height=3, fg='white', bg='green')
    class_id_label.pack()
    classID.pack()
    class_floor_label.pack()
    classFloor.pack()
    button_submit4.pack()
# ===================section window========================



def update_combobox2(event):

    staff_course=Staff.selectid2(sel2.get())
    if len(Staff.selectid2(sel2.get())) == 0: 
        messagebox.showinfo("Message", "No result found for staff id please add staff to teach this course")
    else:
        staff_coursse_selecte=comboBox['values'] =staff_course
        value = event.widget.get()
        return staff_coursse_selecte
 
    
def TopSection():
    top = Toplevel(root)
    top.geometry('300x350')
    global classID
    classID = tk.Entry(top, width=20,)
    global sectionid
    sectionid = tk.Entry(top, width=20,)
    sectionid_label = Label(top, text=" New Section ID:")
    staffid_label = Label(top, text=" Staff ID:")
    courseid_label = Label(top, text=" Course ID:")
    classId_label = Label(top, text=" Class ID:")
    starttime_label = Label(top, text=" Start Time:")
    endtime_label = Label(top, text=" End Time:")
    day_label = Label(top, text=" Day:")
    global start_time
    start_time = tk.Entry(top, width=20,)
    start_time.insert(END, '00:00:00')

    global end_time
    end_time = tk.Entry(top, width=20,)
    end_time.insert(END, '00:00:00')

    #course combobox
    results2 = Course.select()
    results_for_combobox2 = [result2[0] for result2 in results2]
    global sel2
    sel2 = StringVar()
    comboBox2 = ttk.Combobox(top, values=results_for_combobox2, textvariable=sel2)
    comboBox2['values'] = results_for_combobox2
    comboBox2.bind("<<ComboboxSelected>>", lambda event: update_combobox2(event))
   
    #staff combobox
    global comboBox
    global sel
    sel = IntVar()
    comboBox= ttk.Combobox(top,textvariable=sel)

    #class combobox
    results3 = Nclass.select()
    results_for_combobox3 = [result2[0] for result2 in results3]
    global sel3
    sel3 = StringVar()
    comboBox3 = ttk.Combobox(
        top, values=results_for_combobox3, textvariable=sel3)
    #day combobox
    results4 = Day.select()
    results_for_combobox4 = [result4[0] for result4 in results4]
    global sel4
    sel4 = StringVar()
    comboBox4 = ttk.Combobox(
        top, values=results_for_combobox4, textvariable=sel4)
    #button to insert 
    button_submit5 = Button(
        top, text="submit", command=insertSection, width=15, height=3, fg='white', bg='green')

    sectionid_label.place(x=60, y=20)
    sectionid.place(x=150, y=20)
    staffid_label.place(x=90, y=50)
    courseid_label.place(x=80, y=80)
    classId_label.place(x=80, y=120)
    comboBox.place(x=150, y=50)
    comboBox2.place(x=150, y=80)
    comboBox3.place(x=150, y=120)
    starttime_label.place(x=80, y=150)
    endtime_label.place(x=80, y=180)
    start_time.place(x=150, y=150)
    end_time.place(x=150, y=180)
    day_label.place(x=80, y=220)
    comboBox4.place(x=150, y=220)
    button_submit5.place(x=90, y=280)
    # comboBox3.current(0)
    # comboBox.current(0)
    # comboBox2.current(0)
    comboBox4.current(0)
    comboBox4.state(['readonly'])
    comboBox.state(['readonly'])
    comboBox2.state(['readonly'])
    comboBox3.state(['readonly'])
    
# ----------section insert------------

def insertSection():
        newsection = Sction(sectionid.get(), sel2.get(), sel.get(), sel3.get(), start_time.get(), end_time.get(), sel4.get())
        start=re.match(r'^(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)$', start_time.get())
        end =re.match(r'^(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)$', end_time.get())
   
        # print(sectionid.get(), sel2.get(), sel.get(), sel3.get(), start_time.get(), end_time.get(), sel4.get())

        
        if len(sectionid.get()) < 5  or len(sectionid.get()) > 5 or not sectionid.get().isdigit():
            tkinter.messagebox.showinfo(title=None, message="section ID must contain of 5 number and be number ")
        elif  sel3.get() == "":
            tkinter.messagebox.showinfo(title=None, message="Add class ID")
        elif sel2.get() == "":
            tkinter.messagebox.showinfo(title=None, message="Add course ID ")
        elif sel.get() == 0:
            tkinter.messagebox.showinfo(title=None, message="Add staff ID ")
        elif not start:
            tkinter.messagebox.showinfo(title=None, message="time formate is not correct ")
        elif not end:
          tkinter.messagebox.showinfo(title=None, message="time formate is not correct ")



        else:
            end = datetime.strptime(end_time.get(), '%H:%M:%S').time()
            start = datetime.strptime(start_time.get(), '%H:%M:%S').time()
            if (start >= end):
             tkinter.messagebox.showinfo(title=None, message="start time can not be >  end time ")
            else :
                if newsection.check2()==False:
                   tkinter.messagebox.showinfo(title=None, message="There is another section at the same time ")
                elif newsection.checkID()==False:
                    tkinter.messagebox.showinfo(title=None, message="the section ID Linked with another course Try to enter another section ID ") 
                else:
                     newsection.insert2()
                     tkinter.messagebox.showinfo(title=None, message="the section inserted successfully ")
 
        # else:
        # #else  insert the     section id   #sel2=course id  #sel=staff_id #sel3 class                              sel4=day
        # #  newsection = Sction(sectionid.get(), sel2.get(), sel.get(), sel3.get(), start_time.get(), end_time.get(), sel4.get())
        #  print(sel4.get())
        #  newsection.insert()
         
# ==================insert student to Section========


def student_toSection():

    
    student = Student_to_section(sel5.get(), sel6.get())
    
    if student.check()==True:
        messagebox.showinfo("Message", "the student already in this section")

    elif student.check()==False:
        student.insert()
        messagebox.showinfo("Message", "the student was inserted into  section")
    


def sectionR():
    top = Toplevel(root)
    top.geometry('300x350')

    results = Student.select()
    results_for_combobox = [result[0] for result in results]
    global sel5
    sel5 = IntVar()
    comboBox1 = ttk.Combobox(
        top, values=results_for_combobox, textvariable=sel5)

    results2 = Sction.select()
    results_for_combobox = [result[0] for result in results2]
    global sel6
    sel6 = IntVar()
    comboBox2 = ttk.Combobox(
        top, values=results_for_combobox, textvariable=sel6)

    button_submit5 = Button(
        top, text="submit", command=student_toSection, width=15, height=3, fg='white', bg='green')

    studentID_label = Label(top, text=" Student ID:")
    sectionID_label = Label(top, text=" Section ID: ")
    comboBox1.place(x=150, y=50)
    comboBox2.place(x=150, y=80)
    studentID_label.place(x=80, y=50)
    sectionID_label.place(x=80, y=80)
    button_submit5.place(x=90, y=150)
    comboBox2.state(['readonly'])
    comboBox1.state(['readonly'])
    # comboBox2.current(0)
    # comboBox1.current(0)

    # =============attendance report==========


def update_combobox7(event):

    results8 = selectdate(sel9.get())
    if len(selectdate(sel9.get())) == 0: 
        messagebox.showinfo("Message", "No result found for section")
    else:
        result=comboBox7['values'] =results8
        value = event.widget.get()
        return result
def expt1():
    student_=studentidd.get()
    section=sel10.get()
    if len(str(student_))==0:
      tkinter.messagebox.showinfo(title=None, message="add student id")
    elif not studentidd.get().isdigit():
      tkinter.messagebox.showinfo(title=None, message=" student id must be number")
    elif len(str(student_))>10 or len(str(student_))<10 :
      tkinter.messagebox.showinfo(title=None, message=" student id must contain 10 number")
    elif not student_.isdigit():
        messagebox.showinfo("Message", "student id must be number")
    elif len(str(section))==0:
        messagebox.showinfo("Message", "you should add section id")
    
    else:
     print(student_)
     exp(int(student_),sel10.get())
def expt2():
    section=sel9.get()
    date=sel13.get()
    
    if section==0:
        messagebox.showinfo("Message", "you should add section id")
    elif date=="":
        messagebox.showinfo("Message", "you should add date")
    else:
     print(date,section)
     exp2(int(section),date)
     
def allStudint_d():
    top = Toplevel(root)
    top.geometry('300x350')

    button_submit5 = Button(
        top, text="search", command=report, width=15, height=3, fg='white', bg='green')
    button_export2= Button(
        top, text="export to pdf", command=expt2, width=15, height=3, fg='white', bg='green')


    Sectionid_label_lsbel = Label(top, text="Section ID :")

    button_submit5.place(x=100, y=150)
    button_export2.place(x=100, y=200)

    Sectionid_label_lsbel.place(x=50, y=70)

    results5 = selectSection()
    results_for_combobox5 = [results[0] for results in results5]
    global sel9
    sel9 = IntVar()
    global comboBox5
    comboBox5 = ttk.Combobox(
        top, values=results_for_combobox5, textvariable=sel9)
    comboBox5['values'] = results_for_combobox5
    comboBox5.bind("<<ComboboxSelected>>", lambda event: update_combobox7(event))
    
    
    global sel13
    
    sel13 = StringVar()
    global comboBox7
    comboBox7 = ttk.Combobox(top, textvariable=sel13)
    

    comboBox5.state(['readonly'])
    
    comboBox5.place(x=150, y=70)
    comboBox7.state(['readonly'])
    comboBox7.place(x=150, y=100)
    # comboBox5.current(0)
    # comboBox7.current(0)
    root.mainloop()

def forStudint():
    top = Toplevel(root)
    top.geometry('300x350')
    global studentidd
    studentidd = Entry(top, width=20,)
    button_submit5 = Button(
        top, text="search", command=report_, width=15, height=3, fg='white', bg='green')
    studentID_lsbel = Label(top, text="Student ID :")
    Sectionid_label_lsbel = Label(top, text="Section ID :")
    
    
    button_export= Button(
        top, text="export to pdf", command=expt1, width=15, height=3, fg='white', bg='green')

    button_submit5.place(x=100, y=150)
    button_export.place(x=100, y=200)
    studentidd.place(x=150, y=100)
    studentID_lsbel.place(x=50, y=100)
    Sectionid_label_lsbel.place(x=50, y=70)

    results5 = selectSection()
    results_for_combobox4 = [results5[0] for results5 in results5]
    global sel10
    sel10 = IntVar()
    comboBox5 = ttk.Combobox(
        top, values=results_for_combobox4, textvariable=sel10)
    comboBox5.place(x=150, y=70)
    comboBox5.current(0)
    comboBox5.state(['readonly'])
    
    
  



def report():
  date = sel13.get()
  section = sel9.get()

  if date == "" :
    tkinter.messagebox.showinfo(title=None, message="you should enter attendance date")
  elif  section == "":
      tkinter.messagebox.showinfo(title=None, message="you should entre section id")
  elif check3(section)==False:
      tkinter.messagebox.showinfo(title=None, message="there is no section with this id")
  elif check4(section)==False:
      tkinter.messagebox.showinfo(title=None, message="there is no attendance assigned  for this section")
  else:
    res_(section, date)


def report_():
  student = studentidd.get()

  section = sel10.get()
  if len(student)==0:
      tkinter.messagebox.showinfo(title=None, message="add student id")
  elif not studentidd.get().isdigit():
      tkinter.messagebox.showinfo(title=None, message=" student id must be number")
  elif len(student)>10 or len(student)<10 :
      tkinter.messagebox.showinfo(title=None, message=" student id must contain 10 number")
  elif check3(section)==False:
      tkinter.messagebox.showinfo(title=None, message="there is no section with this this id")
  elif check4(section)==False:
      tkinter.messagebox.showinfo(title=None, message="there is no attendance assigned  for this section")
  elif check(student) == False :
    tkinter.messagebox.showinfo(title=None, message="there is no student with this id")
  elif check2(student)==False:
      tkinter.messagebox.showinfo(title=None, message="there is no attendance assigned for this student")
  else:
     res(student, section)

# ------------------------------------------------------------

# ==============training function======================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "My_Dataset")
face_cascade = cv2.CascadeClassifier(
    'cascades/data/haarcascade_frontalface_alt2.xml')
face_cascade2 = cv2.CascadeClassifier(
    'cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()


def train():

    current_id = 0
    label_ids = {}
    y_labels = []
    x_train = []

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                label = os.path.basename(root).replace(" ", "-").lower()
                #print(label, path)
                if not label in label_ids:
                    label_ids[label] = current_id
                    current_id += 1
                id_ = label_ids[label]
                idi_ = label_ids[label]
                # print(label_ids)
                pil_image = Image.open(path).convert("L")  # grayscale
                size = (550, 550)
                final_image = pil_image.resize(size, Image.ANTIALIAS)
                image_array = np.array(final_image, "uint8")
                # print(image_array)
                faces = face_cascade.detectMultiScale(
                    image_array, scaleFactor=1.4, minNeighbors=5)
                facess = face_cascade.detectMultiScale(
                    image_array, scaleFactor=1.1, minNeighbors=5)

                for (x, y, w, h) in facess:
                    roi = image_array[y:y+h, x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)

                for (xi, yi, wi, hi) in faces:
                    roi = image_array[yi:yi+hi, xi:xi+wi]
                    x_train.append(roi)
                    y_labels.append(id_)

    # print(y_labels)
    # print(x_train)

    with open("abels.pickle", 'wb') as f:
        pickle.dump(label_ids, f)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("trainner.yml")
    tkinter.messagebox.showinfo(title=None, message="done")

# take attendance from main class using insert  and insert2 method
def takeAtt():
    takeAttendance.insert()
    # takeAttendance.insert2()
#========================================
def info():
    messagebox.showinfo("Information","Email :ameralashjee@gmail.com")
# ===========main window==============
def update_time():
    global local_dt, local_t
    local_dt = datetime.today().strftime("%A:%Y-%m-%d")
    local_t = datetime.today().strftime('%H:%M:%S')
    local_dt_label = Label(root, fg="black", font=('Times', 25), text=local_dt)
    local_d_label = Label(root, fg="black", font=('Times', 25), text="Time :   "+local_t)
    local_dt_label.config(bg="#EEE9E9")
    local_d_label.config(bg="#EEE9E9")
    local_dt_label.config(text=local_dt)
    local_d_label.config(text="Time :   "+local_t)
    local_dt_label.place(x=80, y=30)
    local_d_label.place(x=80, y=80)
    root.after(1000, update_time)
     # call this function again after 1000 milliseconds (1 second)
root = Tk()
root.after(1000, update_time)
root.geometry('900x900')
button_take_photo = Button(root, text="add new student", command=TopNStudent,
                           width=15, height=3, fg='white', bg='green')
button_take_attendance = Button(
    root, text="take  attendance", command=takeAtt, width=15, height=3, fg='white', bg='green')
button_training = Button(
    root, text="traning the module", command=train, width=15, height=3, fg='white', bg='green')
button_new_staff = Button(
    root, text="add new staff ", command=topstaff, width=15, height=3, fg='black', bg='SteelBlue1')
button_new_course = Button(
    root, text="add new course ", command=Topcourse, width=15, height=3, fg='black', bg='SteelBlue1')
button_new_Class = Button(
    root, text="add new Class ", command=Topcclass, width=15, height=3, fg='black', bg='SteelBlue1')
button_new_section = Button(
    root, text="add new section ", command=TopSection, width=15, height=3, fg='black', bg='SteelBlue1')
button_student_section = Button(
    root, text="section rejestion ", command=sectionR, width=15, height=3, fg='black', bg='SteelBlue1')
button_Report = Button(
    root, text=" Report For Section  ", command=allStudint_d, width=15, height=3, fg='black', bg='RED')
button_Report2 = Button(
    root, text=" Report For Studint  ", command=forStudint, width=15, height=3, fg='black', bg='RED')

# jof = Image.open("jof.png")
# jof = jof.resize((100, 100), Image.ANTIALIAS)
# jof.save("jof.png")
# jof = ImageTk.PhotoImage(file="jof.png")
# label1 = Label(root, image=jof)
# label1.config(bg="#EEE9E9")
# label1.place(relx=0.5, rely=0.4, anchor=CENTER)


root.configure(bg="#EEE9E9")
button_training.place(relx=1, x=-2, y=2, anchor=NE)
button_take_photo.place(relx=1, x=-2, y=60, anchor=NE)
button_take_attendance.place(relx=1, x=-2, y=118, anchor=NE)
button_new_staff.place(relx=1, x=-2, y=180, anchor=NE)
button_new_course.place(relx=1, x=-2, y=239, anchor=NE)
button_new_Class.place(relx=1, x=-2, y=299, anchor=NE)
button_new_section.place(relx=1, x=-2, y=360, anchor=NE)
button_student_section.place(relx=1, x=-2, y=420, anchor=NE)

button_Report.place(relx=1, x=-2, y=600, anchor=NE)
button_Report2.place(relx=1, x=-2, y=670, anchor=NE)

if __name__ == "__main__":
 root.mainloop()

    