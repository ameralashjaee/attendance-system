from conect_to_DB import mycursor
from conect_to_DB import myconn
class Teach():
      def __init__(self, staff_id,course_id):
        self.staff_id = staff_id
        self.course_id = course_id

      def insert(self):

    
           mycursor.execute("INSERT IGNORE INTO teach (staff_id, course_id) VALUES (%s, %s)", (int(self.staff_id),str(self.course_id)))

           myconn.commit()
      def check(self):
        mycursor.execute('select staff_id ,course_id from teach where staff_id=%s and course_id=%s;',(int(self.staff_id),str(self.course_id)))
        result = mycursor.fetchall()
        if result:
          return True
        else:
          return False