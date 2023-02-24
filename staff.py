from conect_to_DB import mycursor
from conect_to_DB import myconn
class Staff():
      def __init__(self, fname, lname, email, staffid):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.staffid = staffid
      
      def insert(self):
          mycursor.execute("INSERT IGNORE INTO staff ( fname, lname, email, staff_id) VALUES (%s, %s, %s, %s)", (str(self.fname),str(self.lname),str(self.email),int(self.staffid)))
          myconn.commit()
      def selectid():
          mycursor.execute('select staff_id from staff;')
          results = mycursor.fetchall()
          return results
      def selectid2(course_id):
          sql='select staff_id from teach where course_id=%s;'
          value=course_id
          mycursor.execute(sql,(str(value),))
          results = mycursor.fetchall()
          return results

      def check(self):
        mycursor.execute('select staff_id from staff where staff_id=%s;',(int(self.staffid),))
        result = mycursor.fetchall()
        if result:
          return True
        else:
          return False
           