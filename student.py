from conect_to_DB import mycursor
from conect_to_DB import myconn
class Student:

#imageid
    def __init__(self, studentid, studentFname, studentLname, email):
        self.studentid = studentid
        self.studentFname = studentFname
        self.studentLname = studentLname
        self.email = email
      
    

    def insert(self):
           mycursor.execute("INSERT  INTO student (student_id, fname, lname, email) VALUES (%s, %s, %s, %s)", (int(self.studentid),str(self.studentFname),str(self.studentLname),str(self.email)))
           myconn.commit()
           print(self.studentid)
   

    def select():
          mycursor.execute('select student_id from student;')
          results = mycursor.fetchall()
          return results
      
    def check(self):
        mycursor.execute('select student_id from student where student_id=%s;',(int(self.studentid),))
        result = mycursor.fetchall()
        if result:
          return True
        else:
          return False