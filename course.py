from conect_to_DB import mycursor
from conect_to_DB import myconn
class Course():
      def __init__(self,  CourseId, Coursename):
        self.CourseId = CourseId
        self.Coursename = Coursename

      def insert(self):
          mycursor.execute("INSERT INTO course ( course_id, course_name) VALUES (%s, %s)", (str(self.CourseId),str(self.Coursename)))
          myconn.commit()
      def select():
          mycursor.execute('select course_id from course;')
          results = mycursor.fetchall()
          return results
      def check(self):
        mycursor.execute('select course_id from  course where course_id=%s;',(str(self.CourseId),))
        result = mycursor.fetchall()
        if result:
          return True
        else:
          return False
           
    
