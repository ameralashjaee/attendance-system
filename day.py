from conect_to_DB import mycursor
from conect_to_DB import myconn
class  Day():
    def select():
          mycursor.execute('select day_name from days;')
          results = mycursor.fetchall()
          return results
 

