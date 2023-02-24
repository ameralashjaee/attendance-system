from conect_to_DB import mycursor
from conect_to_DB import myconn
class StudentPhoto:
     def __init__(self, studentid,  imageid):
        self.studentid = studentid
        self.imageid = imageid

     def insert2(self):
          mycursor.execute("INSERT  INTO student_photos_dir (student_id, URL) VALUES (%s, %s)", (int(self.studentid), str(self.imageid)))
          myconn.commit()
    
     def check(self):
        mycursor.execute('select student_id from student_photos_dir where student_id=%s;',(int(self.studentid),))
        result = mycursor.fetchall()
        if result:
          return True
        else:
          return False
     def check2(self):
        mycursor.execute('select student_id from student where student_id=%s;',(int(self.studentid),))
        result = mycursor.fetchall()
        if result:
          return True
        else:
          return False
