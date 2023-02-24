from conect_to_DB import mycursor
from conect_to_DB import myconn
class  Nclass():
      def __init__(self, className, floor):
        self.className = className
        self.floor = floor

      
      def insert(self):
          mycursor.execute("INSERT IGNORE INTO class ( class_name,floor) VALUES (%s, %s)", (str(self.className),str(self.floor)))
          myconn.commit()
      def select():
          mycursor.execute('select class_name from class;')
          results = mycursor.fetchall()
          return results
      def check(self):
        mycursor.execute('select class_name ,floor from class where class_name=%s and floor=%s;',(str(self.className),str(self.floor)))
        result = mycursor.fetchall()
        if result:
          return True
        else:
          return False