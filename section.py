import tkinter
from conect_to_DB import mycursor
from conect_to_DB import myconn
from datetime import datetime

class Sction():
     def __init__(self, section_id, course_id,stafff_id, class_name, start_time, end_time,day):
        self.section_id = section_id
        self.course_id=course_id
        self.stafff_id = stafff_id
        self.class_name = class_name
        self.start_time = start_time
        self.end_time = end_time
        self.day=day

   #   def insert(self):
      
   #         time_var = datetime.strptime(self.start_time, '%H:%M:%S').time()
   #         time_var2 = datetime.strptime(self.end_time, '%H:%M:%S').time()

   #         sql1="SELECT * FROM section WHERE class_name=%s and day=%s"
   #         mycursor.execute(sql1, (str(self.class_name),str(self.day)))
   #         a=False
   #         if mycursor._rowcount==0:
   #             mycursor.execute("INSERT IGNORE INTO section ( section_id, course_id, staff_id,class_name,start_time,end_time,day) VALUES (%s, %s, %s, %s,%s,%s,%s)", (int(self.section_id),str(self.course_id),int(self.stafff_id),str(self.class_name),time_var,time_var2,str(self.day))) 
   #             myconn.commit()
   #         else:
   #          for results in mycursor: 
   #           try:
   #             y=datetime.strptime(str(results[4]), '%H:%M:%S').time()
   #             z=datetime.strptime(str(results[5]), '%H:%M:%S').time()
   #             d=str(results[6])
            
   #             if (time_var >=y and time_var <= z  and self.day==d):
   #                tkinter.messagebox.showinfo(title="", message="there is another section at this time in the same class "+" day: "+str(d)+"start time: "+str(results[4])+ "end time :"+str(z))
   #                break
   #             elif(time_var2 >= y and time_var2 <= z  and self.day==d):
   #                tkinter.messagebox.showinfo(title="", message="there is another section at this time in the same class "+" day: "+str(d)+"start time: "+str(results[4])+ "end time :"+str(z))
   #                break
   #             elif(time_var < z and time_var2>z and self.day==d):
   #                tkinter.messagebox.showinfo(title="", message="there is another section at this time in the same class "+" day: "+str(d)+"start time: "+str(results[4])+ "end time :"+str(z)) 
   #                break
   #             else:
   #                a=True
                  
   #           except TypeError:
   #             print('TypeError: NoneType object is not subscriptable')
          
   #         if a==True:
   #             mycursor.execute("INSERT IGNORE INTO section ( section_id, course_id, staff_id,class_name,start_time,end_time,day) VALUES (%s, %s, %s, %s,%s,%s,%s)", (int(self.section_id),str(self.course_id),int(self.stafff_id),str(self.class_name),time_var,time_var2,str(self.day))) 
   #             myconn.commit()
           
          
            
     def check(self):
        

         sql1="SELECT * FROM section WHERE class_name=%s and day=%s"
         mycursor.execute(sql1, (str(self.class_name),str(self.day)))
         result = mycursor.fetchall()
         
         
         if result:
            return True
         else:
            return False
      
     def select():
          mycursor.execute('select DISTINCT section_id from section;')
          results = mycursor.fetchall()
          return results
#  ///////////////////////
     def insert2(self):
                     
               time_var = datetime.strptime(self.start_time, '%H:%M:%S').time()
               time_var2 = datetime.strptime(self.end_time, '%H:%M:%S').time()
               mycursor.execute("INSERT IGNORE INTO section ( section_id, course_id, staff_id,class_name,start_time,end_time,day) VALUES (%s, %s, %s, %s,%s,%s,%s)", (int(self.section_id),str(self.course_id),int(self.stafff_id),str(self.class_name),time_var,time_var2,str(self.day))) 
               myconn.commit()
             

          
            
     def check2(self):
          
         time_var = datetime.strptime(self.start_time, '%H:%M:%S').time()
         time_var2 = datetime.strptime(self.end_time, '%H:%M:%S').time()

         sql1="SELECT * FROM section WHERE class_name=%s and day=%s"
         mycursor.execute(sql1, (str(self.class_name),str(self.day)))
         result = mycursor.fetchall()
  
         
         if result :
       
            a=True
            for results in result: 

               y=datetime.strptime(str(results[4]), '%H:%M:%S').time()
               z=datetime.strptime(str(results[5]), '%H:%M:%S').time()
               d=str(results[6])
               if (time_var >= y and time_var <= z  and self.day==d):
                 a=False
               elif(time_var2 >= y and time_var2 <= z  and self.day==d):
                 a=False

               elif(time_var >= z and time_var2 <= z and self.day==d):
                  a=False
               elif(time_var <= z and time_var2 >= z and self.day==d):
                  a=False
               
            return a
            
         else:
            return True
     def  checkID(self):#this will check if the section id linked with another course
         sql1="SELECT * FROM section WHERE section_id=%s "
         mycursor.execute(sql1, (str(self.section_id),))
         result = mycursor.fetchall()
         if result:
           a=True
           for results in result:
            if str(results[0])==self.section_id and str(results[1])==self.course_id:
             a= True
             print(str(results[0])+"=="+self.section_id+str(results[1])+"=="+self.course_id+"  a== "+str(a))
                  
            elif str(results[0])==self.section_id and str(results[1]) != self.course_id:
                     
             a=False
             print(str(results[0])+"=="+self.section_id+str(results[1])+"!="+self.course_id+"a=="+str(a))
           return a

         else:
            a=True
            return a
         
       