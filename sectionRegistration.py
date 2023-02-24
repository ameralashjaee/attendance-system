from conect_to_DB import mycursor
from conect_to_DB import myconn
class Student_to_section:
    def __init__(self, student_id,section_id):
        self.student_id = student_id
        self.section_id = section_id
    def insert(self):

           print(int(self.section_id))
           sql="""INSERT  INTO section_registration (student_Id, section_id, Start_time, End_time, day, class_name)
SELECT student.student_id, section.section_id, section.Start_time, section.End_time, section.day, section.class_name
FROM student
JOIN section ON section_id = section.section_id 
WHERE student.student_id = %s and section.section_id=%s  """
           mycursor.execute(sql, (int(self.student_id),int(self.section_id)))
           myconn.commit()
    def check(self):
#this will check  the student id 
         sql1="SELECT * FROM section_registration WHERE student_Id=%s and  section_id=%s"
         mycursor.execute(sql1, (int(self.student_id),str(self.section_id)))
         result = mycursor.fetchall()
         if result:
                return True
         else:
                return False
