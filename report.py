from tkinter import messagebox
from conect_to_DB import mycursor
from conect_to_DB import myconn
from datetime import datetime
from day import Day
from tkinter import *
from tkinter import ttk
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageBreak
from reportlab.lib.enums import TA_CENTER

def selectSection():
    mycursor.execute("SELECT  section_id From section ")
    results = mycursor.fetchall()
    return results
  
def export(id,attendance_data,count):
 doc = SimpleDocTemplate(str(id)+"_attendance_Report.pdf", pagesize=landscape(letter))

 data=[]
 absent=[]

 data.append(["student_id","status_s","section_id","attendance_date","Start_time","End_time","Class","Day","Date"])
 absent.append(["Absent ",str(count[0])])
 for student in attendance_data:
    data.append(student)

 t=Table(data)
 a=Table(absent)
 # Set the table style
 a.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.gray),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ('BACKGROUND',(0,-1),(-1,-1),colors.beige),
    ('GRID',(0,0),(-1,-1),1,colors.black),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('TEXTCOLOR', (0,0), (-1,-1),colors.red),
    ('ALIGN', (0, 0), (1, 0), 'CENTER'),
]))

 t.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.gray),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND',(0,-1),(-1,-1),colors.beige),
        ('GRID',(0,0),(-1,-1),1,colors.black)
    ]))

 doc.build([a,t])


def export2(id,attendance_data,count1,count2):
 doc = SimpleDocTemplate(str(id)+"_attendance_Report.pdf", pagesize=landscape(letter))

 data=[]
 absent=[]

 data.append(["student_id","status_s","section_id","attendance_date","Start_time","End_time","Class","Day","Date"])
 absent.append(["Absent ",str(count1[0]),"Present  ",str(count2[0])])
 for student in attendance_data:
    data.append(student)

 t=Table(data)
 a=Table(absent)
 # Set the table style
 a.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.gray),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ('BACKGROUND',(0,-1),(-1,-1),colors.beige),
    ('GRID',(0,0),(-1,-1),1,colors.black),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('TEXTCOLOR', (0,0), (-1,-1),colors.red),
    ('ALIGN', (0, 0), (1, 0), 'CENTER'),
]))

 t.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.gray),
        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND',(0,-1),(-1,-1),colors.beige),
        ('GRID',(0,0),(-1,-1),1,colors.black)
    ]))

 doc.build([a,t])


def exp(student_id,section):
  mycursor.execute("SELECT * FROM attendance WHERE student_id=%s  AND section_id=%s",(int(student_id),int(section)))
  expt=mycursor.fetchall()
  mycursor.execute("SELECT  COUNT(*)  FROM attendance WHERE status_s='Absent' AND student_id=%s and section_id=%s  ",(int(student_id),int(section)))
  absent_count = mycursor.fetchall()
  if len(expt)==0:
     messagebox.showinfo("Message", "there is no attendance record for this student")
  else:
   export(student_id,expt,absent_count)
   
def exp2(section,date):
  mycursor.execute("SELECT * FROM attendance WHERE  section_id=%s AND date=%s",(int(section),date))
  results=mycursor.fetchall()
  
  mycursor.execute("SELECT  COUNT(*)  FROM attendance WHERE status_s='Absent' AND  section_id=%s and date=%s ",(int(section),date))
  absent_count = mycursor.fetchall()
  
  mycursor.execute("SELECT  COUNT(*)  FROM attendance WHERE status_s='Present' and date=%s and section_id=%s ",(date,int(section)))
  present_count = mycursor.fetchall()
  
  if len(results)==0:
     messagebox.showinfo("Message", "there is no attendance record for this section")
  else:
   export2(section,results,absent_count,present_count)

 
def res(student_id,section):
    root = Tk()
    root.geometry('1200x1200')
    e=Label(root,width=13,text='Student ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(root,width=13,text='Section ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(root,width=13,text='time attendance',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(root,width=13,text='Status',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(root,width=13,text='Start Time',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=Label(root,width=13,text='End Time',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)     
    e=Label(root,width=13,text='Class name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=6)     
    e=Label(root,width=13,text='Day',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=7)
    e=Label(root,width=13,text='Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=8)
    e=Label(root,width=13,text='Absent_count',borderwidth=2, relief='ridge',anchor='w',bg='red')
    e.grid(row=0,column=9)
    i=2
    
    mycursor.execute("SELECT  COUNT(*)  FROM attendance WHERE status_s='Absent' AND student_id=%s and section_id=%s  ",(int(student_id),int(section)))
    absent_count = mycursor.fetchall()
    if absent_count.count==0:
      absent=0
    else:
         absent=absent_count[0]
    e = Label(root, width=13, text=absent,borderwidth=2, relief='ridge', anchor="w")
    e.grid(row=i, column=9)
    
    mycursor.execute("SELECT * FROM attendance WHERE student_id=%s  AND section_id=%s",(int(student_id),int(section)))

    for student in mycursor: 
     for j in range(len(student)):
       e = Label(root,width=13, text=student[j],
	   borderwidth=2,relief='ridge', anchor="w")
       e.grid(row=i, column=j) 
    
       
     i=i+1
    

   
       

   
def res_(section,date):
   
    root = Tk()
    root.geometry('1200x1200')
    e=Label(root,width=13,text='Student ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(root,width=13,text='Section ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(root,width=13,text='time attendance',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(root,width=13,text='Status',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(root,width=13,text='Start Time',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=Label(root,width=13,text='End Time',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)     
    e=Label(root,width=13,text='Class name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=6)     
    e=Label(root,width=13,text='Day',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=7)
    e=Label(root,width=13,text='Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=8)
    e=Label(root,width=13,text='Present_count',borderwidth=2, relief='ridge',anchor='w',bg='green')
    e.grid(row=0,column=9)
    e=Label(root,width=13,text='Absent_count',borderwidth=2, relief='ridge',anchor='w',bg='red')
    e.grid(row=0,column=10)
    
    i=2
    
    mycursor.execute("SELECT  COUNT(*)  FROM attendance WHERE status_s='Present' and date=%s and section_id=%s ",(date,int(section)))
    present_count = mycursor.fetchall()
    present=0
    if present_count==0 :
     present=0
    else:
          present=present_count[0]
          e = Label(root, width=13, text=present,borderwidth=2, relief='ridge', anchor="w")
          e.grid(row=i, column=9)
          mycursor.execute("SELECT  COUNT(*)  FROM attendance WHERE status_s='Absent' and date=%s and section_id=%s   ",(date,int(section)))
          absent_count = mycursor.fetchall()
          absent=0
          if absent_count==0:
              absent=0
          else:
            absent=absent_count[0]
          e = Label(root, width=13, text=absent,borderwidth=2, relief='ridge', anchor="w")
          e.grid(row=i, column=10)
         
    mycursor.execute("SELECT * FROM attendance WHERE  section_id=%s AND date=%s",(int(section),date))
    results=mycursor.fetchall()
   
    for student in results: 
     for j in range(len(student)):
       e = Label(root,width=13, text=student[j],
	   borderwidth=2,relief='ridge', anchor="w")
       e.grid(row=i, column=j) 
     i=i+1
      
    

def selectdate(section):
          mycursor.execute('SELECT DISTINCT date FROM attendance where section_id=%s',(int(section),))
          results = mycursor.fetchall()
          return results

def check(student_id):
         sql1="SELECT * FROM student WHERE student_id=%s "
         mycursor.execute(sql1, (int(student_id),))
         result = mycursor.fetchall()
         if result:    
           return True
         else:
            return False
def check2(student_id):
         sql1="SELECT * FROM attendance WHERE student_id=%s "
         mycursor.execute(sql1, (int(student_id),))
         result = mycursor.fetchall()
         if result:    
           return True
         else:
            return False
          
def check3(section_id):
         sql1="SELECT * FROM section WHERE section_id=%s "
         mycursor.execute(sql1, (int(section_id),))
         result = mycursor.fetchall()
         if result:    
           return True
         else:
            return False
def check4(section_id):
         sql1="SELECT * FROM attendance WHERE section_id=%s "
         mycursor.execute(sql1, (int(section_id),))
         result = mycursor.fetchall()
         if result:    
           return True
         else:
            return False
      
       
